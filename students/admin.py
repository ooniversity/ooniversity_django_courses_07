from django.contrib import admin
from students.models import Student
from django.db import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'skype']
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    fieldsets = (
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
    )
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': admin.widgets.FilteredSelectMultiple('Courses', False)
        }
    }

    def fullname(self, obj):
        return ("%s %s" % (obj.name, obj.surname))
    fullname.short_description = 'Full name'


admin.site.site_header = 'PyBursa Administration'
admin.site.register(Student, StudentAdmin)