from django.shortcuts import render
from students.models import Student


def list_view(request):
    if 'course_id' in request.GET and request.GET['course_id'] and int(request.GET['course_id']) > 0:
        context = {'students': Student.objects.filter(courses=request.GET['course_id'])}
    else:
        context = {'students': Student.objects.all()}
    return render(request, 'students/list.html', context)

def detail(request, id):
    context = {'student': Student.objects.get(id=id)}
    return render(request, 'students/detail.html', context)
