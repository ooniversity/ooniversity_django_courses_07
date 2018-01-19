from django.contrib import admin
from students.models import Student
from django.forms import widgets
from django.db import models


class StudentAdmin(admin.ModelAdmin):
    admin.site.site_header = "PyBursa Administration"
    list_display = ( 'get_full_name','email','skype')
    search_fields = ['surname','email', ]
    list_filter = ['courses',]

    fieldsets = (( "Personal info",
                  {'fields': ('name', 'surname', 'date_of_birth')}),
                 ('Contact info',
                  {'classes': ('wide',),
                   'fields': ('email', 'phone','address','skype')}),
                 (None, {'fields': ['courses']})
                 )

    filter_horizontal = ('courses',)


admin.site.register(Student, StudentAdmin)

