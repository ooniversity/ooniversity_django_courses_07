from django.shortcuts import render
from courses.models import Course
from .models import Student

def course_list(request):
    c_pk=request.GET.get('course_id',False)
    if not c_pk:
        students=Student.objects.all()
    else:
        course=Course.objects.get(pk=c_pk)
        students=course.student_set.all()
    context={'students':students}
    return render(request,'students/students.html',context)
def student_detail(request,student_id):
    student=Student.objects.get(pk=student_id)
    context={'student':student}
    return render(request,'students/student_detail.html',context)
        
