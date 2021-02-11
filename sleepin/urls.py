from django.urls import path
from django.conf.urls import url
from . import views
from .models import Sleeptime, Meal, Health, Diary


app_name = 'sleepin'
urlpatterns = [
    path('', views.IndexView.as_view(), name="top"),
    path('sleeptime-record/', views.SleeptimeRecordView.as_view(), name="sleeptime_record"),
    path('sleeptime-register/', views.SleeptimeRegisterView.as_view(), name="sleeptime_register"),
    path('sleeptime-detail/<int:pk>/', views.SleeptimeDetailView.as_view(), name="sleeptime_detail"),
    url(r'^sleeptime-calendar/$', views.SleeptimeCalendarView.as_view(model=Sleeptime), name='sleeptime_calendar'),
    path('sleeptime-edit/<int:pk>/', views.SleeptimeEditView.as_view(), name="sleeptime_edit"),
    path('sleeptime-delete/<int:pk>/', views.SleeptimeDeleteView.as_view(), name="sleeptime_delete"),
    path('meal-record/', views.MealRecordView.as_view(), name="meal_record"),
    path('meal-register/', views.MealRegisterView.as_view(), name="meal_register"),
    path('meal-detail/<int:pk>/', views.MealDetailView.as_view(), name="meal_detail"),
    url(r'^meal-calendar/$', views.MealCalendarView.as_view(model=Meal), name='meal_calendar'),
    path('meal-edit/<int:pk>/', views.MealEditView.as_view(), name="meal_edit"),
    path('meal-delete/<int:pk>/', views.MealDeleteView.as_view(), name="meal_delete"),
    path('health-record/', views.HealthRecordView.as_view(), name="health_record"),
    path('health-register/', views.HealthRegisterView.as_view(), name="health_register"),
    path('health-detail/<int:pk>/', views.HealthDetailView.as_view(), name="health_detail"),
    path('health-edit/<int:pk>/', views.HealthEditView.as_view(), name="health_edit"),
    path('health-delete/<int:pk>/', views.HealthDeleteView.as_view(), name="health_delete"),
    url(r'^health-calendar/$', views.HealthCalendarView.as_view(model=Health), name='health_calendar'),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-record/', views.DiaryRecordView.as_view(), name="diary_record"),
    path('diary-register/', views.DiaryRegisterView.as_view(), name="diary_register"),
    path('diary-edit/<int:pk>/', views.DiaryEditView.as_view(), name="diary_edit"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
    url(r'^diary-calendar/$', views.DiaryCalendarView.as_view(model=Diary), name='diary_calendar'),
    path('registered/', views.RegisteredView.as_view(), name="registered"),
]