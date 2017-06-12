from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horizontal = ('courses',)

    fieldsets = (
        ('Personal info', {'fields': ('name', 'surname', 'date_of_birth')}),
        ('Contact info', {'fields': ('email', 'phone', 'address', 'skype')}),
        (None, {'fields': ('courses',)}),
    )

    def full_name(self, obj):
        return u"{} {}".format(obj.name, obj.surname)
    full_name.short_description = 'full name'


admin.site.register(Student, StudentAdmin)
admin.site.site_header = 'PyBursa Administration'

