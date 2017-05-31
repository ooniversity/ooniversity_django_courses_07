from django.contrib import admin
from courses.models import Course,Lesson
from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.db import models

# Register your models here.

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['name','short_description']
    search_fields = ['name']
    fieldsets = [
        (None,{'fields':['name','short_description','description']})
    ]

admin.site.site_header = 'PyBursa Administration'
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson)

