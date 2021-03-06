# Generated by Django 3.1.4 on 2021-01-19 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sleepin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新日時'),
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(verbose_name='登録日')),
                ('sleep_at', models.TimeField(verbose_name='就寝時間')),
                ('wakeup_at', models.TimeField(verbose_name='起床時間')),
                ('satisfaction_level', models.CharField(choices=[('1', 'Excellent'), ('2', 'Good'), ('3', 'Bad')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Sleep',
            },
        ),
    ]
