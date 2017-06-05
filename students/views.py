from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm


def detail(request, student_id):
    context = {
        'student': Student.objects.get(id=student_id),
    }
    return render(request, 'students/detail.html', context)


def list_view(request):
    try:
        course_id = request.GET['course_id']
        student_list = Student.objects.filter(courses=course_id)
    except KeyError:
        student_list = Student.objects.all()

    context = {
        'students_list': student_list,
    }
    return render(request, 'students/list.html', context)


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student %s has been successfully added.' % student.full_name())
            return redirect('students:list_view')
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect(reverse('students:edit', kwargs={'student_id': student_id}))
    else:
        form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, ("Info on %s has been successfully deleted." % student.full_name()))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})