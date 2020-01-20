from django.shortcuts import render
from .models import Course, Lesson
from django.shortcuts import get_object_or_404


def detail(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lessons = get_object_or_404(Lesson, course_id=course_pk)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context=context)
