from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Course, Lesson
from django.contrib import messages
from .forms import CourseModelForm, LessonModelForm


# Create your views here.

def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}

    return render(request, 'index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course_lessons = Lesson.objects.filter(course__id__exact = course_id).order_by('order')
    context = {'course': course, 'course_lessons': course_lessons}

    return render(request, 'courses/detail.html', context)


def create(request):
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Course %s has been successfully added.' % (instance.name))
            return redirect('index')
    else:
        model_form = CourseModelForm()
    context = {'model_form': model_form}
    return render(request, 'courses/add.html', context)


def edit(request, course_id):
    instance = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST, instance=instance)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect(reverse('courses:edit', kwargs={'course_id': instance.id}))
    else:
        model_form = CourseModelForm(instance=instance)
    context = {'model_form': model_form}
    return render(request, 'courses/edit.html', context)


def remove(request, course_id):
    instance = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Course %s has been deleted.' % (instance.name))
        return redirect('index')
    return render(request, 'courses/remove.html')


def add_lesson(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (instance.subject))
            return redirect(reverse('courses:detail', kwargs={'course_id': course.id}))
    else:
        model_form = LessonModelForm(initial={'course': course_id})
    context = {'model_form': model_form}
    return render(request, 'courses/add_lesson.html', context)
