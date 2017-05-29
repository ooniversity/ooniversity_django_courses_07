from django.contrib import admin
from courses.models import Course, Lesson
# Register your models here.
class LessonInline(admin.TabularInline):
    model = Lesson
    list_display = ["subject", "description", "order"]
    fieldsets = [(None, {'fields': ["subject", "description", "order"]})]
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]
    search_fields = ["name"]
    inlines = [LessonInline]
class LessonAdmin(admin.ModelAdmin):
    list_display = ["subject", "description", "order"]
    

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)