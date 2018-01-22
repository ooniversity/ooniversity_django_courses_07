from django.contrib import admin
from .models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender','skype', 'description' ]
    list_filter = ['user__is_staff']

admin.site.register(Coach, CoachAdmin)
# Register your models here.
