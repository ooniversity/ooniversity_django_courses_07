from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentModelForm


def list_view(request):
    if 'course_id' in request.GET and request.GET['course_id'] and int(request.GET['course_id']) > 0:
        context = {'students': Student.objects.filter(courses=request.GET['course_id'])}
        if not context['students'].count():
        	context = {'students': Student.objects.all()}
    else:
        context = {'students': Student.objects.all()}
    return render(request, 'students/list.html', context)

def detail(request, id):
    try:
        context = {'student': Student.objects.get(id=id)}
    except:
        return redirect('students:list_view')
    return render(request, 'students/detail.html', context)

def create(request):
    form = StudentModelForm()
    context = {'form': form}
    return render(request, 'students/add.html', context)