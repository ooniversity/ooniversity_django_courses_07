from django.contrib import admin
from courses.models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    field = ['subject', 'Description', 'Order']
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    inlines = [LessonInline]
    save_on_top = True
    search_fields = ['name']


admin.site.site_header = 'PyBursa Administration'
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
