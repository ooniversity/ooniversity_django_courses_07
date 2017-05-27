from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):
    course_num = Course.objects.get(id=course_id)
    course_shedule = Lesson.objects.filter(course=course_id)
    return render(request, 'courses/detail.html', {'course_num': course_num, 'course_shedule': course_shedule})

def index(request): 
    courses_list = Course.objects.all()
    return render(request, "courses/index.html", {"courses_list": courses_list})
# Create your views here.
