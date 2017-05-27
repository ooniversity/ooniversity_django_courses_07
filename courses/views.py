from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):
    course_inf = Course.objects.get(id=course_id)
    course_plan = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_inf': course_inf, 'course_plan': course_plan})