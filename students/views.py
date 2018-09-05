from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course, Lesson
from students.forms import StudentModelForm


def detail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})

def list_view(request):
    course_id = request.GET.get('course_id', '')
    if course_id == '':
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses=course_id)
    return render(request, 'students/list.html', {'students_list': students_list})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (new_student.name, new_student.surname))
            return redirect('students:list')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            changed_student = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:edit', student.id)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
            messages.success(request, 'Info on %s %s has been successfully deleted.' % (student.name, student.surname))            
            student.delete()
            return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})
