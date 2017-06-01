from django.shortcuts import render ,get_object_or_404
from .models import Student
# Create your views here.


def students_all(request):
    course_id = request.GET.get('course_id')
    if course_id == None or not course_id.isnumeric():
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses__id__exact = course_id)
    template = 'students/list.html'
    context = {'students_list':students_list}
    return render(request,template,context)


def student_detail(request,student_id):
    student_detail = get_object_or_404(Student,pk = student_id)
    template = 'students/detail.html'
    context = {'student_detail':student_detail}
    return render(request,template,context)

