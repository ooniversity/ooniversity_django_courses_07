from django.shortcuts import render,get_object_or_404
from .models import Course,Lesson
from  django.http import HttpResponse
# Create your views here.

def get_all_courses_info(request):
    our_courses = Course.objects.all()
    template = 'index.html'
    return render(request,(template),{"courses_list":our_courses})

def detail(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    template = 'courses/detail.html'
    lessons_per_course = Lesson.objects.filter(course__id__exact=course.id).order_by('order')
    context = {"lessons_list":lessons_per_course,'course':course}
    return render(request,template,context)
