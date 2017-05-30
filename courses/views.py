from django.shortcuts import render
from .models import Course, Lesson


def detail(request, course_id):
    lessons = Lesson.objects.filter(course__id = course_id)
    context = {'lesson_list': lessons}
    return render (request, 'courses/detail.html', context)


# Create your views here.
