from django.contrib import admin
from courses.models import Coach

# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']


admin.site.register(Coach, CoachAdmin)
