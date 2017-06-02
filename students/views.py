from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm


def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses__id=request.GET['course_id'])
    else:
        students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/list.html', context)


def detail(request, id):
    student = Student.objects.get(id=id)
    context = {'student': student}
    return render(request, 'students/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save()
            messages.success(request, "Student %s %s has been successfully added." % (data['name'], data['surname']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
        context = {'form': form}
    return render(request, 'students/add.html', context)


def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            student = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:edit', id=id)
    else:
        form = StudentModelForm(instance=student)
        context = {'form': form}
    return render(request, 'students/edit.html', context)


def remove(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        messages.success(request, "Info on %s %s has been successfully deleted." % (student.name, student.surname))
        student.delete()
        return redirect('students:list_view')
    context = {'student': student}
    return render(request, 'students/remove.html', context)
