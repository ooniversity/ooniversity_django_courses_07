from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm

# Create your views here.

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id == None or not course_id.isnumeric():
        students_list = Student.objects.all()
    else:
        students_list = Student.objects.filter(courses__id__exact = course_id)
    context = {'students_list': students_list}

    return render(request, 'students/list.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}

    return render(request, 'students/detail.html', context)

def create(request):
    if request.method == 'POST':
        model_form = StudentModelForm(request.POST)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Student %s has been successfully added.' % (instance.fullname))
            return redirect('students:list_view')
    else:
        model_form = StudentModelForm()
    context = {'model_form': model_form}
    return render(request, 'students/add.html', context)

def edit(request, student_id):
    instance = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        model_form = StudentModelForm(request.POST, instance=instance)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect(reverse('students:edit', kwargs={'student_id': instance.id}))
    else:
        model_form = StudentModelForm(instance=instance)
    context = {'model_form': model_form}
    return render(request, 'students/edit.html', context)


def remove(request, student_id):
    instance = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Info on %s has been successfully deleted.' % (instance.fullname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html')