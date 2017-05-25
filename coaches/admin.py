from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'skype', 'description']


admin.site.register(Coach, CoachAdmin)
