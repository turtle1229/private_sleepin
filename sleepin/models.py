from accounts.models import CustomUser
from django.db import models
from django.utils import timezone

from flatpickr import DateTimePickerInput, DatePickerInput, TimePickerInput

# Create your models here.
class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title


class Sleeptime(models.Model):
    """睡眠モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    create_date = models.DateField(verbose_name='日付')
    sleep_at = models.TimeField(verbose_name='就寝時間', default='23:00')
    wakeup_at = models.TimeField(verbose_name='起床時間', default='07:00')

    class Meta:
        verbose_name_plural = 'Sleeptime'

    def __str__(self):
        return self.create_date


class Meal(models.Model):
    """食生活モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    create_date = models.DateTimeField(verbose_name='日時', default=timezone.now)
    MEAL_CHOICES = [
        ('食事', '食事'),
        ('飲み物', '飲み物'),
        ('間食', '間食'),
    ]
    meal = models.CharField(verbose_name='食事', choices=MEAL_CHOICES, max_length=30, default='')
    meal_menu = models.CharField(verbose_name='食事内容', max_length=40)

    class Meta:
        verbose_name_plural = 'Meal'

    def __str__(self):
        return self.created_date


class Health(models.Model):
    """ヘルスモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    create_date = models.DateTimeField(verbose_name='日時', default=timezone.now)
    HEALTH_CHOICES = [
        ('トレーニング', 'トレーニング'),
        ('ウォーキング', 'ウォーキング'),
        ('ストレッチ', 'ストレッチ'),
    ]
    health = models.CharField(verbose_name='運動', choices=HEALTH_CHOICES, max_length=30, default='')
    health_menu = models.CharField(verbose_name='運動内容', max_length=40)

    class Meta:
        verbose_name_plural = 'Health'

    def __str__(self):
        return self.created_date
