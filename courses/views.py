from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.
def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.lessons = course.lesson_set.all()
    
    return render(request, 'courses/detail.html', {'course': course})