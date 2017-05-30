from django.shortcuts import render
from .models import Student


def detail(request, student_id):
    student = Student.objects.get(student__id = student_id)
    context = {'student_list': student }
    return render (request, 'students/detail.html', student)

def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id :
        students = Student.objects.filter(course__id = course_id)        
    else:
        students = Student.objects.all()
    context = {'list_view': students}
    return render (request, 'students/list.html', context)




# Create your views here.
