from django.shortcuts import render, get_object_or_404
from .models import Coach

# Create your views here.
def detail(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.coach_crs = coach.coach_courses.all()
    coach.assistant_crs = coach.assistant_courses.all()
    
    return render(request, 'coaches/detail.html', {'coach': coach})