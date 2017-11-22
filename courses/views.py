from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages

# Create your views here.

def index(request):
    courses_list = Course.objects.all()
    context = {'courses_list':courses_list}
    return render(request, 'index.html', context)

def detail(request, cd_id):
    course = get_object_or_404(Course, pk=cd_id)
    lessons = get_list_or_404(Lesson, course_id = course.id)
    return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})


def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            messages.success(request, "Course " + new_course.name + " has been successfully added.")
            return redirect('/')
    return render(request, 'courses/add.html', {'form': form})
        
        
def edit(request, pk):
    course = Course.objects.get(id = pk)
    form = CourseModelForm(instance=course)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', pk=pk)
    return render(request, 'courses/edit.html', {'form': form})
        
    
def remove(request, pk):
    course = Course.objects.get(id = pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course " + course.name + " has been deleted.")
        return redirect('/')
    else:
        return render(request, "courses/remove.html", {'course':course})
        
def add_lesson(request, pk):
    form = LessonModelForm(initial={'course' : Course.objects.get(id=pk)})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, "Lesson " + new_lesson.subject + " has been successfully added.")
            return redirect('courses:detail', cd_id=pk)
    return render(request, 'courses/add_lesson.html', {'form': form})
