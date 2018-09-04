from django.shortcuts import render
from quadratic.forms import QuadraticForm
from math import sqrt


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            context['a'] = a = form.clean_a()
            context['b'] = b = form.cleaned_data['b']
            context['c'] = c = form.cleaned_data['c']
            context['discriminant'] = D = b*b - 4*a*c
            if D == 0:
                context['x']  = -b / (2 * a)
            elif D > 0:
                context['x1'] = (-b + sqrt(D)) / (2 * a)
                context['x2'] = (-b - sqrt(D)) / (2 * a)
    else:
        context = {'form': QuadraticForm()}
    return render(request, 'quadratic/results.html', context)
