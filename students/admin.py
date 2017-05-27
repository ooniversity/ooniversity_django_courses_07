from django.contrib import admin
from . import models
from courses.models import Course


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    search_fields = ('surname', 'email',)
    list_filter = ('courses',)
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
        ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),
        (None, {
            'fields': ('courses',)
        })
    )
    filter_horizontal = ('courses',)
