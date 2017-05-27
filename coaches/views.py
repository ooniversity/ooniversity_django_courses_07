from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from students.models import Student

def detail(request, coach_id):
    coach_info = Coach.objects.get(id=coach_id)
    courses_teacher = Course.objects.filter(coach=coach_id)
    courses_assistant = Course.objects.filter(assistant=coach_id)
    return render(request, 'coaches/detail.html', {'coach_info': coach_info,
                                                    'courses_teacher': courses_teacher,
                                                    'courses_assistant': courses_assistant})


