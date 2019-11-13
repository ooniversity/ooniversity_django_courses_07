from django.shortcuts import render
from .models import Course,Lesson

def by_course(request,course_id):
    course=Course.objects.get(pk=course_id)
    lessons=course.lesson_set.all()
    context={'course':course,'lessons':lessons}
    return render(request,'courses/by_course.html',context)
    

