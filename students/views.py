from django.shortcuts import render
from .models import Student
from django.shortcuts import get_list_or_404, get_object_or_404


def list_view(request):
    course_id = request.GET.get('course_id')
    students = Student.objects.filter(courses=course_id) if course_id else Student.objects.all()
    context = {'students': students}
    return render(request, 'students/list.html', context=context)


def detail(request, student_pk):
    student = get_object_or_404(Student, id=student_pk)
    context = {'student': student}
    return render(request, 'students/detail.html', context=context)
