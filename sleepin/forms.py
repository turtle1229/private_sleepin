from django import forms
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import Sleeptime, Meal, Health, Diary


class SleeptimeRegisterForm(forms.ModelForm):
    class Meta:
        model = Sleeptime
        fields = ('create_date', 'sleep_at', 'wakeup_at')
        widgets = {
            'create_date': DatePickerInput(
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'sleep_at': TimePickerInput(),
            'wakeup_at': TimePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MealRegisterForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('create_date', 'meal_menu', 'meal')
        labels = {
            'create_date': '',
            'meal_menu': '',
            'meal': '',
        }
        widgets = {
            'create_date': DateTimePickerInput(
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class HealthRegisterForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ('create_date', 'health_menu', 'health')
        labels = {
            'create_date': '',
            'health_menu': '',
            'health': '',
        }
        widgets = {
            'create_date': DateTimePickerInput(
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DiaryRegisterForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('created_at', 'title', 'content', 'photo1', 'photo2', 'photo3')
        widgets = {
            'created_at': DateTimePickerInput(
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
