from django.shortcuts import render, get_object_or_404
from .models import Coach


def detail(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    context = {'coach': coach}
    return render(request, 'coaches/detail.html', context)

# Create your views here.
