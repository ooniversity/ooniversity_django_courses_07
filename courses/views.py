from django.shortcuts import render
from .models import Course, Lesson


def detail(request, id):
    """Для отображения информации о курсе"""
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})
