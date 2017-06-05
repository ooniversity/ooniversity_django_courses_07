from django.shortcuts import render
from math import sqrt
from quadratic.forms import QuadraticForm


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def quadratic_results(request):
    context = {}

    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if not a:
                context['a_error'] = 'коэффициент не определен'
            elif not is_number(a):
                context['a_error'] = 'коэффициент не целое число'
            else:
                a = int(a)

            if not b:
                context['b_error'] = 'коэффициент не определен'
            elif not is_number(b):
                context['b_error'] = 'коэффициент не целое число'
            else:
                b = int(b)

            if not c:
                c = 0
            elif not is_number(c):
                context['c_error'] = 'коэффициент не целое число'
            else:
                c = int(c)

            if a == 0:
                context['a_error'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

            if len(context) == 0:
                discriminant = b * b - 4 * a * c
                if discriminant > 0:
                    x1 = (-b + sqrt(discriminant)) / (2 * a)
                    x2 = (-b - sqrt(discriminant)) / (2 * a)
                    solution = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
                elif discriminant == 0:
                    x1 = (-b - sqrt(discriminant))/(2 * a)
                    solution = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % (x1)
                else:
                    solution = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений'

                context['solution'] = solution
                context['discriminant'] = discriminant

            context['a'] = a
            context['b'] = b
            context['c'] = c

    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'results.html', context)
