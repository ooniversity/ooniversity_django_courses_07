from django.shortcuts import render
from students.models import Student


def detail(request, student_id):
    context = {
        'student': Student.objects.get(id=student_id),
    }
    return render(request, 'students/detail.html', context)


def list_view(request):
    try:
        course_id = request.GET['course_id']
        student_list = Student.objects.filter(courses=course_id)
    except KeyError:
        student_list = Student.objects.all()

    context = {
        'students_list': student_list,
    }
    return render(request, 'students/list.html', context)
