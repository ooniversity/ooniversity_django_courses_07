from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
def index(request):
    courses = Course.objects.all()
    return render(request,'index.html',{'Courses':courses})

def detail(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    lessons = Lesson.objects.filter(course__id=course_id)
    return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})

#Добавлении курса
def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Course " + instance.name + " has been successfully added.")
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request,'courses/add.html',{'form':form})

#Изменении курса
def edit(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            messages.success(request,"The changes have been saved.")
            return redirect('/courses/edit/'+course_id)
    else:
        form = CourseModelForm(instance=course)
    return render(request,'courses/edit.html',{'form':form})

#Удаления курса
def remove(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method=="POST":
        course.delete()
        messages.success(request, "Course " + course.name + " has been deleted.")
        return redirect('/')
    return render(request,'courses/remove.html',{'course':course})

#Добавления урока
def add_lesson(request,course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Lesson " + instance.subject + " has been successfully added.")
            return redirect('/courses/'+course_id)
    else:
        form = LessonModelForm(initial={'course':course_id})
    return render(request,'courses/add.html',{'form':form})