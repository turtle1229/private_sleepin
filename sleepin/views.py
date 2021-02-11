from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe

import itertools
import calendar
from django.contrib import messages
from .forms import DiaryRegisterForm, SleeptimeRegisterForm, MealRegisterForm, HealthRegisterForm
from .models import Sleeptime, Meal, Health, Diary
from .utils import Sleeptime_list, Meal_list, Health_list, Diary_list
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from django.utils.timezone import localtime, make_aware
from django.urls import reverse_lazy, reverse


# Create your views here.

class IndexView(generic.TemplateView):
    """トップ画面ビュー"""

    template_name = "top.html"


class SleeptimeRecordView(LoginRequiredMixin, generic.TemplateView):
    """睡眠時間画面を表示するビュー"""
    model = Sleeptime
    template_name = 'sleeptime_record.html'


class SleeptimeRegisterView(LoginRequiredMixin, generic.CreateView):
    """睡眠時間登録画面ビュー"""
    model = Sleeptime
    template_name = 'sleeptime_register.html'
    form_class = SleeptimeRegisterForm
    success_url = reverse_lazy('sleepin:registered')

    def form_valid(self, form):
        sleeptime = form.save(commit=False)
        sleeptime.user = self.request.user
        sleeptime.save()
        messages.success(self.request, '睡眠時間を記録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "睡眠時間の記録に失敗しました")
        return super().form_invalid(form)


class SleeptimeDetailView(generic.DetailView):
    """睡眠時間詳細画面ビュー"""

    model = Sleeptime
    template_name = 'sleeptime_detail.html'


class SleeptimeEditView(LoginRequiredMixin, generic.UpdateView):
    """睡眠時間編集ビュー"""

    model = Sleeptime
    template_name = 'sleeptime_edit.html'
    form_class = SleeptimeRegisterForm

    def get_success_url(self):
        return reverse_lazy('sleepin:sleeptime_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '睡眠時間を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "睡眠時間の更新に失敗しました。")
        return super().form_invalid(form)


class SleeptimeDeleteView(LoginRequiredMixin, generic.DeleteView):
    """睡眠時間削除ビュー"""

    model = Sleeptime
    template_name = 'sleeptime_delete.html'
    success_url = reverse_lazy('sleepin:sleeptime_calendar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "睡眠時間を削除しました。")
        return super().delete(request, *args, **kwargs)


class SleeptimeCalendarView(generic.ListView):
    """睡眠時間カレンダービュー"""

    model = Sleeptime
    template_name = 'sleeptime_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        cal = Sleeptime_list(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class MealRecordView(LoginRequiredMixin, generic.TemplateView):
    """食事画面を表示するビュー"""

    model = Meal
    template_name = 'meal_record.html'


class MealRegisterView(LoginRequiredMixin, generic.CreateView):
    """食事登録画面ビュー"""

    model = Meal
    template_name = 'meal_register.html'
    form_class = MealRegisterForm
    success_url = reverse_lazy('sleepin:registered')

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user = self.request.user
        meal.save()
        messages.success(self.request, '食事を記録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "食事の記録に失敗しました")
        return super().form_invalid(form)


class MealDetailView(generic.DetailView):
    """食事詳細ビュー"""

    model = Meal
    template_name = 'meal_detail.html'


class MealEditView(LoginRequiredMixin, generic.UpdateView):
    """食事編集ビュー"""

    model = Meal
    template_name = 'meal_edit.html'
    form_class = MealRegisterForm

    def get_success_url(self):
        return reverse_lazy('sleepin:meal_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '食事を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "食事の更新に失敗しました。")
        return super().form_invalid(form)


class MealDeleteView(LoginRequiredMixin, generic.DeleteView):
    """食事削除ビュー"""

    model = Meal
    template_name = 'meal_delete.html'
    success_url = reverse_lazy('sleepin:meal_calendar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "食事を削除しました。")
        return super().delete(request, *args, **kwargs)


class MealCalendarView(generic.ListView):
    """食事カレンダービュー"""

    model = Meal
    template_name = 'meal_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Meal_list(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class HealthRecordView(LoginRequiredMixin, generic.TemplateView):
    """運動画面を表示するビュー"""

    model = Health
    template_name = 'health_record.html'


class HealthRegisterView(LoginRequiredMixin, generic.CreateView):
    """運動登録画面ビュー"""

    model = Health
    template_name = 'health_register.html'
    form_class = HealthRegisterForm
    success_url = reverse_lazy('sleepin:registered')

    def form_valid(self, form):
        health = form.save(commit=False)
        health.user = self.request.user
        health.save()
        messages.success(self.request, '運動を記録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "運動の記録に失敗しました")
        return super().form_invalid(form)


class HealthDetailView(generic.DetailView):
    """運動詳細ビュー"""

    model = Health
    template_name = 'health_detail.html'


class HealthEditView(LoginRequiredMixin, generic.UpdateView):
    """運動編集ビュー"""

    model = Health
    template_name = 'health_edit.html'
    form_class = HealthRegisterForm

    def get_success_url(self):
        return reverse_lazy('sleepin:health_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '運動を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "運動の更新に失敗しました。")
        return super().form_invalid(form)


class HealthDeleteView(LoginRequiredMixin, generic.DeleteView):
    """運動削除ビュー"""

    model = Health
    template_name = 'health_delete.html'
    success_url = reverse_lazy('sleepin:health_calendar')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "運動を削除しました。")
        return super().delete(request, *args, **kwargs)


class HealthCalendarView(generic.ListView):
    """運動カレンダービュー"""

    model = Health
    template_name = 'health_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        cal = Health_list(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class DiaryListView(LoginRequiredMixin, generic.ListView):
    """日記一覧ビュー"""

    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


class DiaryRecordView(LoginRequiredMixin, generic.TemplateView):
    """日記画面を表示するビュー"""

    model = Diary
    template_name = 'diary_record.html'


class DiaryRegisterView(LoginRequiredMixin, generic.CreateView):
    """日記登録画面ビュー"""

    model = Diary
    template_name = 'diary_register.html'
    form_class = DiaryRegisterForm
    success_url = reverse_lazy('sleepin:registered')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました")
        return super().form_invalid(form)


class DiaryDetailView(generic.DetailView):
    """日記詳細ビュー"""
    model = Diary
    template_name = 'diary_detail.html'


class DiaryEditView(LoginRequiredMixin, generic.UpdateView):
    """日記編集ビュー"""

    model = Diary
    template_name = 'diary_edit.html'
    form_class = DiaryRegisterForm

    def get_success_url(self):
        return reverse_lazy('sleepin:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    """日記削除ビュー"""

    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('sleepin:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)


class DiaryCalendarView(generic.ListView):
    """日記カレンダービュー"""

    model = Diary
    template_name = 'diary_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        cal = Diary_list(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class RegisteredView(generic.TemplateView):
    template_name = 'registered.html'
