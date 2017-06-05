from django.shortcuts import render
from math import sqrt
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    context = {}

    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            discriminant = b * b - 4 * a * c

            if discriminant > 0:
                context['x1'] = (-b + sqrt(discriminant)) / (2 * a)
                context['x2'] = (-b - sqrt(discriminant)) / (2 * a)
            elif discriminant == 0:
                context['x1'] = (-b - sqrt(discriminant))/(2 * a)

            context['discriminant'] = discriminant

    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'results.html', context)
