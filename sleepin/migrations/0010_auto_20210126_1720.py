# Generated by Django 3.1.4 on 2021-01-26 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sleepin', '0009_auto_20210125_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='diary_content',
        ),
        migrations.RemoveField(
            model_name='event',
            name='diary_title',
        ),
        migrations.AddField(
            model_name='event',
            name='diary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sleepin.diary', verbose_name='日記'),
        ),
    ]