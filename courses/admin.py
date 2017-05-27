from django.contrib import admin
from courses.models import Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'course']
    
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)