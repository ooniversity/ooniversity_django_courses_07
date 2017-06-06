from django.shortcuts import render, redirect, reverse, get_object_or_404
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages

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
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            text_for_success = 'Student ' + data['name'] + ' ' + data['surname'] + ' has been successfully added.'
            messages.success(request, (text_for_success))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    instance = get_object_or_404(Student, pk=student_id)
    form = StudentModelForm(instance=instance)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect(reverse('students:edit', kwargs={'student_id': instance.id}))
    else:
        form = StudentModelForm(instance=instance)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    remove_student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        text_for_success = 'Info on ' + str(remove_student.name) + ' ' + str(remove_student.surname) + ' has been successfully deleted.'
        remove_student.delete()
        messages.success(request, (text_for_success))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'remove_student': remove_student})
