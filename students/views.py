from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id == None or not course_id.isnumeric():
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses__id__exact = course_id)
    context = {'students_list': students_list}

    return render(request, 'students/list.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}

    return render(request, 'students/detail.html', context)