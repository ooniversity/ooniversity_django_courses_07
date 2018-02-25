from django.shortcuts import render
from coaches.models import Coach

def detailview(request, pk):
    coach_curr = Coach.objects.get(id=pk)
    return render(request, 'coaches/detail.html',     context = {'coach_curr': coach_curr })
