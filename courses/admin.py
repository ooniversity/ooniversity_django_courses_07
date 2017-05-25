from django.contrib import admin
from .models import Course, Lesson

admin.site.register(Course)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'course', 'order')