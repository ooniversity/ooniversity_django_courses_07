from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            student = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
            messages.success(request, ('Student %s has been successfully added.' % student))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
        context = {'form': form}
    return render(request, 'students/add.html', context)


def edit(request, id):
    student = Student.objects.get(id=id)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, ('Info on the student has been successfully changed.'))
            return redirect('students:edit', id=id)
    context = {'form': form}
    return render(request, 'students/edit.html', context)


def remove(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        student_name = student.name + ' ' + student.surname
        messages.success(request, ("Info on %s has been successfully deleted." % student_name))
        return redirect('students:list_view')
    context = {'student': student}
    return render(request, 'students/remove.html', context)


def list_view(request):
    if request.GET:
            n = request.GET[u'course_id']
            stud = Student.objects.filter(courses=int(n))
            context = {'stud': stud}
            return render(request, 'students/list.html', context)
    stud = Student.objects.all()
    context = {"stud": stud}
    return render(request, 'students/list.html', context)


def detail(request, pk):
    stud = Student.objects.get(id__exact = int(pk))
    context = { "stud": stud }
    return render(request, 'students/detail.html', context)