from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from courses.models import Course


def detail(request, student_id):
    student_info = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student_info': student_info})
    
def list_view(request):
    without_c = False
    try:
        course_id = request.GET['course_id']
    except KeyError:
        without_c = True
        
    if without_c == True:
        students_list = Student.objects.all
        active_course = None
    else:
        students_list = Student.objects.filter(courses=course_id)
        active_course = Course.objects.get(id=course_id)
    
    return render(request, 'students/list.html', {'st_list': students_list})