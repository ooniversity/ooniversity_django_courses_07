from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from students.forms import StudentModelForm
from django.contrib import messages


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

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
            messages.success(request, "Student %s has been successfully added."%instance.name)
            return redirect ('students:list_view')       
    else:
        form = StudentModelForm()   
    context = {'form': form}
    return render (request, 'students/add.html', context)

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect ('students:edit', student.id)       
    else:
        form = StudentModelForm(instance=student)   
    context = {'form': form}
    return render (request, 'students/edit.html', context)

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s has been successfully deleted."%student.name)
        return redirect ('students:list_view')
    print(redirect ('index'))
    context = {'student': student}
    return render (request, 'students/remove.html', context)


# Create your views here.
