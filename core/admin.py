from django.contrib import admin
from .models import *

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','firstname','age',)

admin.site.register(Work,WorkAdmin)
