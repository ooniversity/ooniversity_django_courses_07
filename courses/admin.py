from django.contrib import admin
from django.db import models
from courses.models import Course, Lesson, Student

class CourseAdmin(admin.ModelAdmin):
	list_display = ["name", "short_description", "description"]

class LessonAdmin(admin.ModelAdmin):
	list_display = ["subject", "description", "course", "order"]

class StudentAdmin(admin.ModelAdmin):
	list_display = ["name", "surname", "date_of_birth", "email", "phone", "adress", "skype", "get_courses"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)
# Register your models here.
