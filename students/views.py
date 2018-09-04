from django.shortcuts import render
from .models import Student
from courses.models import Course, Lesson 


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})

def list_view(request):
    course_id = request.GET.get('course_id', '')
    if course_id == '':
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses=course_id)
    return render(request, 'students/list.html', {'students_list': students_list})
