# Generated by Django 3.1.4 on 2021-01-25 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sleepin', '0008_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='health_menu',
            field=models.CharField(default='', max_length=40, verbose_name='運動内容'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_menu',
            field=models.CharField(default='', max_length=40, verbose_name='食事内容'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('diary_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diary_content', to='sleepin.diary', verbose_name='本文')),
                ('diary_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diary_title', to='sleepin.diary', verbose_name='タイトル')),
                ('health_health_menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='health_health_menu', to='sleepin.health', verbose_name='運動内容')),
                ('meal_meal_menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='meal_meal_menu', to='sleepin.meal', verbose_name='食事内容')),
                ('sleeptime_sleep_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sleeptime_sleep_at', to='sleepin.sleeptime', verbose_name='就寝時間')),
                ('sleeptime_wakeup_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sleeptime_wakeup_at', to='sleepin.sleeptime', verbose_name='起床時間')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
