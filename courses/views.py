from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'lessons': Lesson.objects.filter(course=id).order_by('order'),
    }
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 
                'Course %s has been successfully added.' % form.cleaned_data['name'])
            return redirect('index')
    else:
        form = CourseModelForm(initial={'coach': 1})
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', id=id)
    else:
        form = CourseModelForm(instance=course)
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course.name)
        return redirect('index')
    context = {'course': course}
    return render(request, 'courses/remove.html', context)


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 
                'Lesson %s has been successfully added.' % form.cleaned_data['subject'])
            return redirect('courses:detail', id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)