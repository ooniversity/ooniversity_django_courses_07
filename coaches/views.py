from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id): 

    coach_obj = Coach.objects.get(id=coach_id)
    courses_coach = Course.objects.filter(coach=coach_id)
    courses_assistant = Course.objects.filter(assistant=coach_id)

    return render(request, "coaches/detail.html", {"coach": coach_obj, "courses_coach": courses_coach, "courses_assistant": courses_assistant })

