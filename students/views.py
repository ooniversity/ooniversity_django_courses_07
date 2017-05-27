from django.shortcuts import render
from students.models import Student


def detail(request, student_id):
    student_info = Student.objects.get(id=student_id)
    courses_list = student_info.courses.all()
    return render(request, 'students/detail.html', {'student_info': student_info, 'courses_list': courses_list})
    
def list_view(request): 

    course_id = request.GET.get('course_id', '')
    
    if course_id == '':
        student_list = Student.objects.all()
    else:
        student_list = Student.objects.filter(courses=course_id)

    return render(request, "students/list.html", {"student_list": student_list })

# Create your views here.