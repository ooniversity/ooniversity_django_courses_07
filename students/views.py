from django.shortcuts import render
from .models import Student
# Create your views here.


def students_all(request):
    all_students = Student.objects.all()
    template = 'student_list.html'
    context = {'students_list':all_students}
    return render(request,(template),context)
def student_detail(request):
    pass
