from django.shortcuts import render
from math import sqrt


def index(request):
    return render(request, 'index.html')


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def arg_validate(data, key: str):
    arg = data.get(f'{key}')
    result = {key: arg}
    if arg:
        if is_integer(arg):
            result[key] = int(arg)
        else:
            result[f'{key}_error'] = 'коэффициент не целое число'
    else:
        result[f'{key}_error'] = 'коэффициент не определен'
    return result


def root_equation(content):
    a = content.get('a')
    b = content.get('b')
    c = content.get('c')
    if a and b and c:
        discriminant = b * b - 4 * a * c

        if discriminant == 0:
            x = - b / 2 * a
            message = f'Дискриминант равен нулю, квадратное уравнение ' \
                      f'имеет один действительный корень: x1 = x2 = {x}'

        elif discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / 2 * a
            x2 = (-b - sqrt(discriminant)) / 2 * a
            message = f'Квадратное уравнение имеет два действительных корня: ' \
                      f'x1 = {round(x1, ndigits=1)}, x2 = {round(x2, ndigits=1)}'

        else:
            message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        return {'discriminant': discriminant, 'message': message}
    return {}


def quadratic_results(request):
    arg_list = ['a', 'b', 'c']
    content = {}
    data = request.GET

    if data:
        for key in arg_list:
            content.update(arg_validate(data, key))

        if data['a'] == '0':
            content['a_error'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

        if not any('error' in key for key in content.keys()):
            content.update(root_equation(content))
    else:
        content = dict.fromkeys(['a_error', 'b_error', 'c_error'], 'коэффициент не определен')

    return render(request, 'results.html', content)
