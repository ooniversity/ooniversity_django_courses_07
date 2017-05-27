from django.shortcuts import render
from coaches.models import Coach


def detail(request, coach_id):
    
    return render(request, 'courses/detail.html')




# Create your views here.
