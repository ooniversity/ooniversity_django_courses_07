from django.shortcuts import render
from .models import Coach

def detail(request,coach_id):
    coach=Coach.objects.get(pk=coach_id)
    context={'coach':coach,'courses_coach':coach.coach_courses.all(),
             'courses_assistant':coach.assistant_courses.all()}
    return render(request,'coaches/detail.html',context)
