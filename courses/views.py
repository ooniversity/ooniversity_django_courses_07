from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            course = form.cleaned_data['name']
            messages.success(request, ('Course %s has been successfully added.' % course))
            return redirect('index')
    else:
        form = CourseModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, id):
    course = Course.objects.get(id=id)
    form = CourseModelForm(instance=course)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, ('The changes have been saved.'))
            return redirect('courses:edit', id=id)
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, ('Course %s has been deleted.' % course.name))
        return redirect('index')
    context = {'course': course}
    return render(request, 'courses/remove.html', context)


def add_lesson(request, id):
    course = Course.objects.get(id=id)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject']
            messages.success(request, ('Lesson %s has been successfully added.' % subject))
            return redirect('courses:detail', id)
    context = {'form': form, 'course': course}
    return render(request, 'courses/add_lesson.html', context)


def index(request):
    courses = Course.objects.all()
    context = {"cour": courses}
    return render(request, 'index.html', context)


def detail(request, pk):
    one_course = Course.objects.get(id__exact = int(pk))
    lessons = Lesson.objects.filter(course__id__exact = int(pk))
    context = {"course": one_course, "lessons": lessons}
    return render(request, 'courses/detail.html', context)
