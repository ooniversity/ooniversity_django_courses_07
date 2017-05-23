from django.shortcuts import render,get_object_or_404
from courses.models import Course, Lesson

def index(request):
    courses = Course.objects.all()
    return render(request,'courses/index.html',{'Courses':courses})

def detail(request,course_id):
    course = get_object_or_404(Course,id=course_id)
    lessons = Lesson.objects.filter(course__id=course_id)
    return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})