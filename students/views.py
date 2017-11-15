from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Student
# Create your views here.

def list_view(request):
    if request.GET:    
        param=request.GET
        course_id = param['course_id']
        list_st = Student.objects.filter(courses=course_id)
            
    else: 
        list_st = Student.objects.all()
    
    return render(request, 'list.html', {'list_st':list_st})

def detail(request, st_id):
    student_detail = Student.objects.get(id=st_id)
    return render(request, 'detail.html', {'student_detail':student_detail})
