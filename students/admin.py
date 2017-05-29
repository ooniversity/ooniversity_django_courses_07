from django.contrib import admin
from students.models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['surname','name']

# Register your models here.
admin.site.register(Student,AdminStudent)
