from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            context['a'] = a = form.clean_a()
            context['b'] = b = form.cleaned_data['b']
            context['c'] = c = form.cleaned_data['c']
            context['discriminant'] = D = b**2-4*a*c
            if D == 0:
                context['x']  = -1*b/(2*a)
            elif D > 0:
                context['x1'] = (-1*b + D**0.5)/(2*a)
                context['x2'] = (-1*b - D**0.5)/(2*a)
    else:
        context = {'form': QuadraticForm()}
    return render(request, 'quadratic/results.html', context)
