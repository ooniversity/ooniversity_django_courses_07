from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student
from courses.models import Course
from .forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def detail(request, student_id):
    student_info = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student_info': student_info})
    
def list_view(request):
    without_c = False
    try:
        course_id = request.GET['course_id']
    except KeyError:
        without_c = True
        
    if without_c == True:
        students_list = Student.objects.all
        active_course = None
    else:
        students_list = Student.objects.filter(courses=course_id)
        active_course = Course.objects.get(id=course_id)
    
    return render(request, 'students/list.html', {'st_list': students_list})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            text_for_success = 'Student ' + data['name'] + ' ' + data['surname'] + ' has been successfully added.'
            messages.success(request, text_for_success)
            return redirect("/students/")
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    edit_student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=edit_student)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            text_for_success = 'Info on the student has been successfully changed.'
            messages.success(request, text_for_success)
            return render(request, 'students/edit.html', {'form': form})
    else:
        form = StudentModelForm(instance=edit_student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    remove_student = Student.objects.get(id=student_id)
    if request.method == "POST":
        text_for_success = 'Info on ' + str(remove_student.name) + ' ' + str(remove_student.surname) + ' has been successfully deleted.'
        messages.success(request, text_for_success)
        remove_student.delete()
        return redirect("/students/")
    else:
        return render(request, 'students/remove.html', {'remove_student': remove_student})


