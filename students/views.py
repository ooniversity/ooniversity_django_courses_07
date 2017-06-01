from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm


def list_view(request):
    context = {}
    if 'course_id' in request.GET and request.GET['course_id'] and int(request.GET['course_id']) > 0:
        context['students'] = Student.objects.filter(courses=request.GET['course_id'])
        if not context['students'].count():
        	context['students'] = Student.objects.all()
    else:
        context['students'] = Student.objects.all()
    return render(request, 'students/list.html', context)


def detail(request, id):
    try:
        context = {'student': Student.objects.get(id=id)}
    except:
        return redirect('students:list_view')
    return render(request, 'students/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data.get('surname') + ' ' + form.cleaned_data.get('name')
            messages.success(request, 'Student %s has been successfully added.' % fullname)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context= {'form': form}
    return render(request, 'students/add.html', context)


def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:edit', id=id)
    else:
        form = StudentModelForm(instance=student)
    context = {'form': form}
    return render(request, 'students/edit.html', context)


def remove(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        fullname = student.name + ' ' + student.surname
        student.delete()
        messages.success(request, 'Info on %s has been successfully deleted.' % fullname)
        return redirect('students:list_view')

    context = {'student': student}
    return render(request, 'students/remove.html', context)