from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Student
from courses.models import Course, Lesson 


def detail(request, number):
    template_name = 'students/detail.html'
    student = Student.objects.filter(id=number)
    return render(request, template_name, {'student': student[0]})

def list_view(request):
    course_number = request.GET.get('course_id', '')
    template_name = 'students/list.html'
    if course_number == '':
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses=course_number)
    return render(request, template_name, {'students_list': [students_list[i] for i in range(len(students_list))]})
