from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def index(request):
    context = {'courses_list': Course.objects.all()}
    return render(request, 'index.html', context)


def detail(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
        'lessons_list': Lesson.objects.filter(course_id=course_id),
    }

    return render(request, 'courses/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % course)
            return redirect('index')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect(reverse('courses:edit', kwargs={'course_id': course_id}))
    else:
        form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, ("Course %s has been deleted." % course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, course_id):
    get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson)
            return redirect(reverse('courses:detail', kwargs={'course_id': course_id}))
    else:
        form = LessonModelForm(initial={'course': course_id})

    return render(request, 'courses/add.html', {'form': form})
