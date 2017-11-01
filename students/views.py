from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.
def list_view(request):
    get = request.GET.dict()
    course_id = None
    students = Student.objects.all()
    
    if get and get['course_id']:
        students = students.filter(courses__id=get['course_id']).all()
        course_id = get['course_id']
        
    if students:
        for student in students:
            student.crs = student.courses.all()
        
    return render(request, 'students/list.html', {'students': students, 'course_id': course_id})


def detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.crs = student.courses.all()
    
    return render(request, 'students/detail.html', {'student': student})