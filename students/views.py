from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.



def list_view(request):
    if request.GET:    
        param=request.GET
        course_id = param['course_id']
        list_st = Student.objects.filter(courses=course_id)
            
    else: 
        list_st = Student.objects.all()
    
    return render(request, 'students/list.html', {'list_st':list_st})

def detail(request, st_id):
    student_detail = Student.objects.get(id=st_id)
    return render(request, 'students/detail.html', {'student_detail':student_detail})


def create(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, "Student " + new_student.name + " " + new_student.surname + " has been successfully added.")
            return redirect('/students/')
    return render(request, 'students/add.html', {'form': form})
        
        
def edit(request, pk):
    student = Student.objects.get(id = pk)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:edit', pk=pk)
    return render(request, 'students/edit.html', {'form': form})
        
    
def remove(request, pk):
    student = Student.objects.get(id = pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Info on " + student.name + " " + student.surname + " has been successfully deleted.")
        return redirect('/students/')
    else:
        return render(request, "students/remove.html", {'student':student})
