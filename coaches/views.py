from django.shortcuts import render
from .models import Coach


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coaches/detail.html', {'coach': coach})
