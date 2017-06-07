from django.shortcuts import render, redirect, get_object_or_404, reverse
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def detail(request, course_id):
    course_inf = Course.objects.get(id=course_id)
    trainer = {'f_name': course_inf.coach.user.first_name, 
                'l_name': course_inf.coach.user.last_name,
                'descr': course_inf.coach.description,
                'id': course_inf.coach.id}
    assistant = {'f_name': course_inf.assistant.user.first_name, 
                'l_name': course_inf.assistant.user.last_name,
                'descr': course_inf.assistant.description,
                'id': course_inf.assistant.id}
    print(assistant)
    course_plan = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_inf': course_inf, 'course_plan': course_plan,
                                                    'trainer': trainer, 'assistant': assistant})

def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, ('Course %s has been successfully added.' % data['name']))
            return redirect("index")
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    edit_course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=edit_course)
        if form.is_valid():
            form.save()
            text_for_success = 'The changes have been saved.'
            messages.success(request, text_for_success)
            return redirect('courses:edit', course_id=course_id)
    else:
        form = CourseModelForm(instance=edit_course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    instance = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, 'Course %s has been deleted.' % (instance.name))
        return redirect('index')
    return render(request, 'courses/remove.html')


def add_lesson(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (instance.subject))
            return redirect(reverse('courses:detail', kwargs={'course_id': course.id}))
    else:
        form = LessonModelForm(initial={'course': course.id})
    return render(request, 'courses/add_lesson.html', {'form': form})