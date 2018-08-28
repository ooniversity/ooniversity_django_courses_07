from django.shortcuts import render
from .models import Course, Lesson


def detail(request, course_id):
    context = {'course': Course.objects.get(id=course_id)}
    context['lesson_list'] = Lesson.objects.filter(course=context['course'])
    return render(request, 'courses/detail.html', context)



