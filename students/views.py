from django.shortcuts import render
from students.models import Student
from courses.models import Course

def student_list(request):
    if 'course_id' in request.GET:
        qsstud_list = Student.objects.filter(courses = request.GET['course_id'])
    else:
        qsstud_list = Student.objects.all()
    return render(request, 'students/list.html', context = {'qsstud_list': qsstud_list})

def student_detail(request, pk):
    qscurrent = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', context = {'qscurrent': qscurrent })
