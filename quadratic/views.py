from django.shortcuts import render
from math import sqrt
# Create your views here.

def quadratic_results(request):
    str = ''
    x1 = ''
    x2 = ''

    errors = {
        'error_a' : '',
        'error_b' : '',
        'error_c' : '',
    }

    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    if not a:
        errors['error_a'] = 'коэффициент не определен'
    if not b:
        errors['error_b'] = 'коэффициент не определен'
    if not c:
        c = 0
    if a:
        try:
            a = int(a)
        except ValueError:
            errors['error_a'] = 'коэффициент не целое число'
    if b:
        try:
            b = int(b)
        except ValueError:
            errors['error_b'] = 'коэффициент не целое число'
    if c:
        try:
            c = int(c)
        except ValueError:
            errors['error_c'] = 'коэффициент не целое число'

    if not errors['error_a'] and not errors['error_b']:

        d = b*b - 4*a*c
        if d > 0:
            x1 = (-b + sqrt(d))/(2*a)
            x2 = (-b - sqrt(d))/(2*a)
            str = 'Дискриминант: %s, Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (d, x1, x2)
        elif d == 0:
            x1 = (-b - sqrt(d))/(2*a)
            str = 'Дискриминант: 0, Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %f' % (x1)
        else:
            str = 'Дискриминант: %s, Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений' % (d)

    data = {
        'a': a,
        'b': b,
        'c': c,
        'str': str,
        'errors': errors,
        'x1': x1,
        'x2': x2
    }
    return render(request, 'quadratic/results.html', data)

