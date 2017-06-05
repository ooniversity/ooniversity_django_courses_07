from django.shortcuts import render
from courses.models import Course, Lesson


def index(request):
    context = {'courses_list': Course.objects.all()}
    return render(request, 'index.html', context)


def detail(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
        'lessons_list': Lesson.objects.filter(course_id=course_id),
    }

    return render(request, 'courses/detail.html', context)
