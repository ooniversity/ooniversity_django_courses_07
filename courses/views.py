from django.shortcuts import render
from .models import Course, Lesson
from .forms import CourseModelForm

def detail(request, id):
    """Для отображения информации о курсе"""
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)


def add(request):
    pass


def edit(request, id):
    pass


def remove(request, id):
    pass

