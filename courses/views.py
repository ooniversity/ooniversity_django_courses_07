from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Course, Lesson


def detail(request, number):
    template_name = 'courses/detail.html'
    course = Course.objects.filter(id=number)
    lesson_list = Lesson.objects.filter(course=course[0])
    return render(request, template_name, {'course': course[0], 'lesson_list': [lesson_list[i] for i in range(len(lesson_list))]})



