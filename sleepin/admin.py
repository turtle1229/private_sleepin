from django.contrib import admin

# Register your models here.
from .models import Diary
from .models import Sleeptime
from .models import Meal
from .models import Health
from .models import Event

admin.site.register(Diary)
admin.site.register(Sleeptime)
admin.site.register(Meal)
admin.site.register(Health)
admin.site.register(Event)