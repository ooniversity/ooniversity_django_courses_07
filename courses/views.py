from django.shortcuts import render, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detailview(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'courses/detail.html', {'course': course})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mess_suc = 'Course %s has been successfully added.' % form.cleaned_data['name']
            messages.success(request, mess_suc)
            return redirect('/')
    else:
        form = CourseModelForm()           
    context = {'form': form}
    return render(request, 'courses/add.html', context)
    
def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            mess_suc = 'The changes have been saved.'
            messages.success(request, mess_suc)
            return redirect('/courses/edit/'+pk)
    else:
        form = CourseModelForm(instance=course)           
    context = {'form': form}
    return render(request, 'courses/edit.html', context)    
    
def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        mess_suc = 'Course %s has been deleted.' % course.name
        course.delete()
        messages.success(request, mess_suc)
        return redirect('/')
    context = {'course': course}
    return render(request, 'courses/remove.html', context)
    
def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mess_suc = 'Lesson %s has been successfully added.' % form.cleaned_data['subject']
            messages.success(request, mess_suc)
            return redirect('/courses/'+pk)
    else:
        form = LessonModelForm(initial={'course': pk})           
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)
