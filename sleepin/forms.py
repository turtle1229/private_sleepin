from django import forms
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import Sleeptime
from .models import Meal
from .models import Health
from .models import Diary

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください。'

class DiaryRegisterForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('created_at', 'title', 'content', 'photo1', 'photo2', 'photo3')
        widgets = {
            'created_at' : DateTimePickerInput(
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


class SleeptimeRegisterForm(forms.ModelForm):
    class Meta:
        model = Sleeptime
        fields = ('create_date', 'sleep_at', 'wakeup_at')
        widgets = {
            'create_date' : DatePickerInput(
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'sleep_at' : TimePickerInput(),
            'wakeup_at' : TimePickerInput()
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
            'create_date' : '',
            'meal_menu' : '',
            'meal' : '',
        }
        widgets = {
            'create_date' : DatePickerInput(
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
            'create_date' : '',
            'health_menu' : '',
            'health' : '',
        }
        widgets = {
            'create_date' : DatePickerInput(
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