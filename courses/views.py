from django.shortcuts import render
from courses.models import Course, Lesson
# Create your views here.

def detail(request, course_id):
    course_info = Course.objects.get(id=course_id)
    course_plan = Lesson.objects.filter(courses=course_id)
    return render(request, 'courses/detail.html', {'course_info': course_info, 'course_plan': course_plan})