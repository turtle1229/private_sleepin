from django.urls import path

from . import views


app_name = 'sleepin'
urlpatterns = [
    path('', views.IndexView.as_view(), name="top"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('sleeptime-record/', views.SleeptimeRecordView.as_view(), name="sleeptime_record"),
    path('sleeptime-register/', views.SleeptimeRegisterView.as_view(), name="sleeptime_register"),
    path('meal-record/', views.MealRecordView.as_view(), name="meal_record"),
    path('meal-register/', views.MealRegisterView.as_view(), name="meal_register"),
    path('health-record/', views.HealthRecordView.as_view(), name="health_record"),
    path('health-register/', views.HealthRegisterView.as_view(), name="health_register"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-record/', views.DiaryRecordView.as_view(), name="diary_record"),
    path('diary-register/', views.DiaryRegisterView.as_view(), name="diary_register"),
    path('registered/', views.RegisteredView.as_view(), name="registered"),
]