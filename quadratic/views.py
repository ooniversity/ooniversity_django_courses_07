from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    form = QuadraticForm(request.GET)
    context = {'form': form}
    if form.is_valid():
        data = form.cleaned_data
        context = dict(list(context.items()) + list(data.items()))
        a = context['a']
        b = context['b']
        c = context['c']
        D = b**2-4*a*c
        context['discriminant'] = D
        if D == 0:
            context['x']  = -1*b/(2*a)
        elif D > 0:
            context['x1'] = (-1*b + D**0.5)/(2*a)
            context['x2'] = (-1*b - D**0.5)/(2*a)
    return render(request, 'quadratic/results.html', context)
