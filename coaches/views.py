from django.shortcuts import render, redirect
from .models import Coach
from courses.models import Course


def detail(request, id):
    try:
        context = {
            'coach': Coach.objects.get(id=id),
            'teacher': Course.objects.filter(coach=id),
            'assistant': Course.objects.filter(assistant=id)
        }
    except:
        return redirect('/')
    return render(request, 'coaches/detail.html', context)