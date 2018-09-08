from django.contrib import admin
from students.models import Student
from django.db import models
from django.forms import widgets


class StudentAdmin(admin.ModelAdmin):
    
    def full_name(obj):
        return obj.name + ' ' + obj.surname

    list_display = [full_name, "email", "skype"]
    search_fields = ["surname", "email"]
    list_filter = ["courses"]
    fieldsets = [
                ('Personal info', {'fields': ["name", "surname", "date_of_birth"]}),
                ('Contact info',  {'fields': ["email", "phone", "address", "skype"]}),
                (None,            {'fields': ["courses"]}),
                ]

    formfield_overrides = {
                            models.ManyToManyField: {'widget': widgets.SelectMultiple}
                           }


admin.site.register(Student, StudentAdmin)
