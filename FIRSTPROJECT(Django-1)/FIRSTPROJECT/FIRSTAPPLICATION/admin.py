from django.contrib import admin

# Register your models here.
from .models import SeniorStudents
from .models import SophomoreStudents
from .models import JuniorStudents

admin.site.register(JuniorStudents)
admin.site.register(SophomoreStudents)
admin.site.register(SeniorStudents)