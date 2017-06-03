from django.shortcuts import render
from math import sqrt
from .forms import QuadraticForm
# Create your views here.

def quadratic_results(request):
    context = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            a = data['a']
            b = data['b']
            c = data['c']
            d = b * b - 4 * a * c
            context['d'] = d
            if d > 0:
                x1 = (-b + sqrt(d)) / (2 * a)
                x2 = (-b - sqrt(d)) / (2 * a)
                context['x1'] = x1
                context['x2'] = x2
            elif d == 0:
                x1 = (-b - sqrt(d)) / (2 * a)
                context['x1'] = x1

    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'quadratic/results.html', context)