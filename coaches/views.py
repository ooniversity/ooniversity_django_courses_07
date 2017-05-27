from django.shortcuts import render
from .models import Coach
from courses.models import Course

def detail(request, id):
    coach = Coach.objects.get(id=id)
    coach.coaches_courses
    context = {'coach': coach}

    return render(request, 'coaches/detail.html', context)
