from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Student
from . import forms

# Create your views here.
def list_view(request):
    get = request.GET.dict()
    course_id = None
    students = Student.objects.all()
    
    if get and get['course_id']:
        students = students.filter(courses__id=get['course_id']).all()
        course_id = get['course_id']
        
    if students:
        for student in students:
            student.crs = student.courses.all()
        
    return render(request, 'students/list.html', {'students': students, 'course_id': course_id})


def detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.crs = student.courses.all()
    
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    form = forms.StudentModelForm()
    
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST)
        
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Student {} {} has been successfully added.'.format(instance.name, instance.surname))
            
            return redirect('/students/')
    
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = forms.StudentModelForm(instance=student)
    
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            
            return redirect(reverse('students:update', kwargs={'student_id': student.id}))

    return render(request, 'students/edit.html', {'form': form})
    
    
def remove(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on {} {} has been successfully deleted.'.format(student.name, student.surname))
        
        return redirect('/students/')
    
    return render(request, 'students/remove.html', {'student': student})
    