from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from courses.models import Course
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
            student = form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']
            messages.success(request, 'Student %s has been successfully added.' % student)
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