from django.shortcuts import render
from .models import Student
from courses.models import Course

def student_list(request):
    if 'course_id' in request.GET:
        course = Course.objects.get(pk=request.GET['course_id'])
        students = Student.objects.filter(courses=course)
    else:
        students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/students_detail.html', {'student': student})
