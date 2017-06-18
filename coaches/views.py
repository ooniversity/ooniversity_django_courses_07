from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from students.models import Student

def detail(request, coach_id):
    coach = Coach.objects.get(id__exact = int(coach_id))
    context = {"coach_info": coach}
    return render(request, 'coaches/detail.html', context)
   