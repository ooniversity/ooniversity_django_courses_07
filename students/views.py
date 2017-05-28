from django.shortcuts import render, get_object_or_404
from students.models import Student

def list_view(request):
    course_id = request.GET.get('course_id',None)
    if course_id:
        students = Student.objects.filter(courses__id=course_id)
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def detail(request,student_id):
    student = get_object_or_404(Student,pk=student_id)
    return render(request,'students/detail.html',{'student':student})