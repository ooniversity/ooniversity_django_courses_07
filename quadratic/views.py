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
            if d > 0:
                x1 = (-b + sqrt(d)) / (2 * a)
                x2 = (-b - sqrt(d)) / (2 * a)
                Discriminant = 'Дискриминант: %s, Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (d, x1, x2)
            elif d == 0:
                x1 = (-b - sqrt(d)) / (2 * a)
                Discriminant = 'Дискриминант: 0, Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %f' % (x1)
            else:
                Discriminant = 'Дискриминант: %s, Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений' % (d)

            context['Discriminant'] = Discriminant
    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'quadratic/results.html', context)