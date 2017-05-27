from django.shortcuts import render
from coaches.models import Coach

def detail(request, coach_id): 

    coach_obj = Coach.objects.get(id=coach_id)
    #courses_list = student_obj.courses.all()
    #student_list

    return render(request, "coaches/detail.html", {"coach": coach_obj }) #, "courses_list": courses_list

