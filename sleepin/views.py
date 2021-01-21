from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from.forms import InquiryForm
from .forms import InquiryForm, DiaryRegisterForm, SleeptimeRegisterForm, MealRegisterForm, HealthRegisterForm
from .models import Sleeptime
from .models import Meal
from .models import Health
from .models import Diary
from django.urls import reverse_lazy
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "top.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm

class SleeptimeRecordView(LoginRequiredMixin, generic.TemplateView):
    model = Sleeptime
    template_name = 'sleeptime_record.html'

class SleeptimeRegisterView(LoginRequiredMixin, generic.CreateView):
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

class MealRecordView(LoginRequiredMixin, generic.TemplateView):
    model = Meal
    template_name = 'meal_record.html'

class MealRegisterView(LoginRequiredMixin, generic.CreateView):
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

class HealthRecordView(LoginRequiredMixin, generic.TemplateView):
    model = Health
    template_name = 'health_record.html'

class HealthRegisterView(LoginRequiredMixin, generic.CreateView):
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

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class DiaryDetailView(generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

class DiaryRecordView(LoginRequiredMixin, generic.TemplateView):
    model = Diary
    template_name = 'diary_record.html'

class DiaryRegisterView(LoginRequiredMixin, generic.CreateView):
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

class RegisteredView(generic.TemplateView):
    template_name = "registered.html"