from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'course']
    
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)