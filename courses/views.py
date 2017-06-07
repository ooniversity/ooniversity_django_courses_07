from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def index(request):

    courses_list = Course.objects.all()
    return render(request, "index.html", {"courses_list": courses_list})


def detail(request, course_id):

    #course_obj = Course.objects.get(id=course_id)
    course = get_object_or_404(Course, id=course_id)

    lessons_list = course.lesson_set.all()  #course_obj.lesson_set.all
    #lessons_list = Lesson.objects.filter(course=course_id)
    return render(request, "courses/detail.html", {"course": course, "lessons_list": lessons_list })


def add(request):

    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Course %s has been successfully added." % instance.name)
            return redirect('index')
    else:
         form = CourseModelForm()

    return render(request, "courses/add.html", {'form': form })


def edit(request, pk):

    #course = Course.objects.get(id=pk)
    course = get_object_or_404(Course, id=pk)

    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', pk = course.id)
            return render(request, "courses/edit.html", {'form': form })
    else:
        form = CourseModelForm(instance=course)

    return render(request, "courses/edit.html", {'form': form })


def remove(request, pk):

    #course = Course.objects.get(id=pk)
    course = get_object_or_404(Course, id=pk)

    if request.method == "POST":
        course.delete()
        messages.success(request, "Course %s has been deleted." % course.name)
        return redirect('index')
    else:
        form = CourseModelForm(instance=course)

    return render(request, "courses/remove.html", {'form': form })


def add_lesson(request, course_id):

    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.course = Course.objects.get(id=course_id)
            instance.save()
            messages.success(request, "Lesson %s has been successfully added." % instance.subject)
            return redirect('courses:detail', course_id = course_id)
    else:
         form = LessonModelForm(initial={'course': course_id, })

    return render(request, "courses/add_lesson.html", {'form': form })
