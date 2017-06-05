from django.contrib import admin

from .models import Course, Lesson


class LessonInline(admin.TabularInline):
	model = Lesson
	extra = 0


class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
	list_display = ('subject', 'description')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)




