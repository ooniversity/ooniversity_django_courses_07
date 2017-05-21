from  django.contrib import admin
from courses.models import Course,Lessons
from students.models import Student

admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(Student)
