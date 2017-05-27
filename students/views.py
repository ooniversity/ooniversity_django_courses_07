from django.shortcuts import render
from .models import Student
from courses.models import Course

def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses__id=request.GET['course_id'])
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/list.html', context)

def detail(request, id):
    student = Student.objects.get(id=id)
    context = {'student': student}
    return render(request, 'students/detail.html', context)
