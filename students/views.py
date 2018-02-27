from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def student_list(request):
    if 'course_id' in request.GET:
        qsstud_list = Student.objects.filter(courses = request.GET['course_id'])
    else:
        qsstud_list = Student.objects.all()
    return render(request, 'students/list.html', context = {'qsstud_list': qsstud_list})

def student_detail(request, pk):
    qscurrent = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', context = {'qscurrent': qscurrent })

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mess_suc = 'Student %s %s has been successfully added.' % (form.cleaned_data['name'], form.cleaned_data['surname'])
            messages.success(request, mess_suc)
            return redirect('/students/')
    else:
        form = StudentModelForm()           
    context = {'form': form}
    return render(request, 'students/add.html', context)
    
def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            mess_suc = 'Info on the student has been successfully changed.'
            messages.success(request, mess_suc)
            return redirect('/students/edit/'+pk)
    else:
        form = StudentModelForm(instance=student)           
    context = {'form': form}
    return render(request, 'students/edit.html', context)    
    
def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        mess_suc = 'Info on %s %s has been successfully deleted.' % (student.name, student.surname)
        student.delete()
        messages.success(request, mess_suc)
        return redirect('/students/')
    context = {'student': student}
    return render(request, 'students/remove.html', context)  
