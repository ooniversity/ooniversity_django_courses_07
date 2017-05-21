from django.shortcuts import render
from math import sqrt


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def quadratic_results(request):
    data = {}

    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    if not a:
        data['a_error'] = 'коэффициент не определен'
    if not b:
        data['b_error'] = 'коэффициент не определен'
    if not c:
        c = 0

    if not is_number(a):
        data['a_error'] = 'коэффициент не целое число'
    if not is_number(b):
        data['b_error'] = 'коэффициент не целое число'
    if not is_number(c):
        data['c_error'] = 'коэффициент не целое число'

    if a == 0:
        data['a_error'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    a = int(a)
    b = int(b)
    c = int(c)

    if len(data) == 0:
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

        data['solution'] = solution
        data['discriminant'] = discriminant


    data['a'] = a
    data['b'] = b
    data['c'] = c


    return render(request, 'results.html', data)
