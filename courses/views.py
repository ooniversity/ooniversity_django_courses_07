from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Course, Lesson

# Create your views here.

def index(request):
    courses_list = Course.objects.all()
    context = {'courses_list':courses_list}
    return render(request, 'index.html', context)

def detail(request, cd_id):
    course = get_object_or_404(Course, pk=cd_id)
    lessons = get_list_or_404(Lesson, course_id = course.id)
    return render(request, 'courses/detail.html', {'course':course, 'lessons':lessons})
