from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm

def detail(request, id):
    """
    Детальная информация о курсе
    """
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course=course)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save()
            messages.success(request, "Course %s has been successfully added." % data['name'])
            return redirect('index')
    else:
        form = CourseModelForm()
        context = {'form': form}
    return render(request, 'courses/add.html', context)


def add_lesson(request, id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            instance = form.save()
            messages.success(request, "Lesson %s has been successfully added." % data['subject'])
            return redirect('courses:detail', id=id)
    else:
        form = LessonModelForm()
        context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)


def edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        context = {'form': form}
        if form.is_valid():
            data = form.cleaned_data
            student = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', id=id)
    else:
        form = CourseModelForm(instance=course)
        context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        messages.success(request, "Course %s has been deleted." % course.name)
        course.delete()
        return redirect('index')
    context = {'course': course}
    return render(request, 'courses/remove.html', context)

