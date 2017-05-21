from django.shortcuts import render
from django.http import HttpResponse
from math import sqrt

def quadratic_results(request): 
    a = {'value': request.GET.get('a', ''), 'message': '', 'ok': True}
    b = {'value': request.GET.get('b', ''), 'message': '', 'ok': True}
    c = {'value': request.GET.get('c', ''), 'message': '', 'ok': True}
    d = {'value': None, 'message': ''}

    check_param(a)
    check_param(b)
    check_param(c)

    if a['value'] == 0:
        a['message'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        a['ok'] = False

    if a['ok'] and b['ok'] and c['ok']:
        d['value'] = b['value']*b['value'] - 4*a['value']*c['value']
        if d['value'] > 0:
            x1 = (-1 * b['value'] + sqrt(d['value'])) / (2 * a['value'])
            x2 = (-1 * b['value'] - sqrt(d['value'])) / (2 * a['value'])
            d['message'] = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)
        elif d['value'] == 0:
            x1 = (-1 * b['value'] + sqrt(d['value'])) / (2 * a['value'])
            d['message'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % (x1)
        else:
            d['message'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

    return render(request, "results.html", { 'a': a, 'b': b, 'c': c, 'd': d, })


def check_param(param):
    if param['value'] == '':
        param['message'] = 'коэффициент не определен'
        param['ok'] = False
    else:
        try:
            param['value'] = int(param['value'])
        except:
            param['message'] = 'коэффициент не целое число'
            param['ok'] = False
    
