from django.contrib import admin
from students.models import Student
from django.db import models
from django.forms import widgets

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal info',   {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info',    {'fields': ['email', 'phone', 'address', 'skype']}),
        (None,              {'fields': ['courses']})
        ]
    list_display = ['full_name','email', 'skype']
    search_fields = ['surname']
    
    formfield_overrides = {
        models.ManyToManyField: {'widget': widgets.SelectMultiple}
}

admin.site.register(Student, StudentAdmin)
