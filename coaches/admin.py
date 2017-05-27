from django.contrib import admin
from.models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description')
    list_filter = ['user__is_staff']

    def first_name(self, obj):
        return obj.user.first_name

    first_name.short_description = 'first_name'

    def last_name(self, obj):
        return obj.user.last_name

    last_name.short_description = 'last_name'
