from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    return render (request, 'courses/detail.html', context)


# Create your views here.
