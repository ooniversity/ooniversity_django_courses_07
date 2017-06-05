from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    return render (request, 'courses/detail.html', context)

def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
            messages.success(request, "Lesson %s has been successfully added."%instance.subject)
            return redirect ('courses:detail', course.id)       
    else:
        form = LessonModelForm(initial = {'course': course})   
    context = {'form': form}
    return render (request, 'courses/add_lesson.html', context)

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print(instance)
            messages.success(request, "Course %s has been successfully added."%instance.name)
            return redirect ('index')       
    else:
        form = CourseModelForm()   
    context = {'form': form}
    return render (request, 'courses/add.html', context)

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect ('courses:edit', course.id)       
    else:
        form = CourseModelForm(instance=course)   
    context = {'form': form}
    return render (request, 'courses/edit.html', context)

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted."%course.name)
        return redirect ('index')
    print(redirect ('index'))
    context = {'course': course}
    return render (request, 'courses/remove.html', context)


# Create your views here.
