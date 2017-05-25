from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


def detail(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'lessons': Lesson.objects.filter(course=id).order_by('order'),
    }
    return render(request, 'courses/detail.html', context)