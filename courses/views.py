from django.shortcuts import render
from courses.models import Course, Lesson


def list_view(request):

    courses_list = Course.objects.all()
    return render(request, "courses/list.html", {"courses_list": courses_list})


def detail(request, course_id):

    course_obj = Course.objects.get(id=course_id)
    #lessons_list = course_obj.lesson_set.all()  #course_obj.lesson_set.all
    lessons_list = Lesson.objects.filter(course=course_id)
    return render(request, "courses/detail.html", {"course": course_obj, "lessons_list": lessons_list })
