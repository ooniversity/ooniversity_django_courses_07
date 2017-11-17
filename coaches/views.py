from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Coach
from students.models import Student
from courses.models import Course

def detail(request, cc_id):
    coach = get_object_or_404(Coach, pk=cc_id)
    courses_coach = Course.objects.filter(coach_id = cc_id)
    courses_assist = Course.objects.filter(assistant_id = cc_id)
    return render(request, 'coaches/detail.html', {'coach':coach, 'courses_coach':courses_coach, 'courses_assist':courses_assist})  
    
