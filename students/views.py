from django.shortcuts import render, get_object_or_404
from .models import Student


def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student }
    return render (request, 'students/detail.html', context)

def list_view(request):
    course_id = request.GET.get('course_id', None)
    if course_id :
        students = Student.objects.filter(courses__id=course_id)        
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render (request, 'students/list.html', context)




# Create your views here.
