from django.shortcuts import render
from .models import Coach


def detail(request, id):
    coach = Coach.objects.get(id=id)
    context = {'coach': coach}

    return render(request, 'coaches/detail.html', context)
