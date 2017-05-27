from django.contrib import admin
from.models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'surname', 'gender', 'skype', 'description')
    list_filter = ['user__is_staff']
