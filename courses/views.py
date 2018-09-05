from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    context = {'course': Course.objects.get(id=course_id)}
    context['lesson_list'] = Lesson.objects.filter(course=context['course'])
    return render(request, 'courses/detail.html', context)

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % new_course.name)
            return redirect('index')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {'form': form})

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request, 'Course %s has been deleted.' % course.name)            
        course.delete()
        return redirect('index')

    return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % new_lesson.subject)
            return redirect('courses:detail', course.id )
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})

