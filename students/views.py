from django.shortcuts import render
from .models import Student
from django.shortcuts import get_list_or_404


def list_view(request):
    students = get_list_or_404(Student)
    context = {'students': students}
    return render(request, 'students/list.html', context=context)