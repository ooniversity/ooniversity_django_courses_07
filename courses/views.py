from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Coach


# Create your views here.

def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}

    return render(request, 'index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course_lessons = Lesson.objects.filter(course__id__exact = course_id).order_by('order')
    context = {'course': course, 'course_lessons': course_lessons}

    return render(request, 'courses/detail.html', context)