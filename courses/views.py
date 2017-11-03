from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course
from .forms import CourseModelForm, LessonModelForm

# Create your views here.
def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.lessons = course.lesson_set.all()
    
    return render(request, 'courses/detail.html', {'course': course, 'course_id': course.id})


def add(request):
    form = CourseModelForm()
    
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Course {} has been successfully added.'.format(form.cleaned_data['name']))
            
            return redirect('index')
    
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseModelForm(instance=course)
    
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            
            return redirect('courses:edit', course_id=course.id)
    
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course {} has been deleted.'.format(course.name))
        
        return redirect('index')
    
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, course_id):
    form = LessonModelForm(initial={'course': course_id})
    
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson {} has been successfully added.'.format(form.cleaned_data['subject']))
            
            return redirect('courses:detail', course_id=course_id)  
    
    return render(request, 'courses/add_lesson.html', {'form': form})