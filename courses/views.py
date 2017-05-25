from django.shortcuts import render
#from django.urls import reverse
from courses.models import Course, Lesson


def index(request): 

    courses_list = Course.objects.all()
    return render(request, "courses/index.html", {"courses_list": courses_list})


def courses(request, course_id): 

    course_obj = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course_id)
    return render(request, "courses/courses.html", {"course": course_obj, "lessons_list": lessons_list })


