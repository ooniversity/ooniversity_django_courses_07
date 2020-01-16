from django.shortcuts import render
from math import sqrt


class Argument:

    def __init__(self, arg_name, arg_value):
        self.name = arg_name
        self.value = arg_value
        self.value_int = None
        self.error_message = None

    def valid(self):
        if not self.value:
            self.error_message = 'коэффициент не определен'
            return False

        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = 'коэффициент не целое число'
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_message = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            return False
        return True


def get_discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def get_eq_root(a, b, d, order=1):
    return (-b + sqrt(d)) / 2 * a if order == 1 else (-b - sqrt(d)) / 2 * a


def quadratic_results(request):
    context = {'error': False}
    arg_name_list = ['a', 'b', 'c']

    for arg_name in arg_name_list:
        argument = Argument(arg_name, request.GET.get(arg_name, ''))
        if argument.valid():
            context[arg_name] = argument.value_int
        else:
            context['error'] = True
            context[f'{arg_name}_error'] = argument.error_message
            context[arg_name] = argument.value

    if not context['error']:
        a = context['a']
        b = context['b']
        c = context['c']
        d = get_discriminant(a, b, c)

        if d < 0:
            result_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            x = - b / 2 * a
            result_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: ' \
                             f'x1 = x2 = {x}'
        else:
            x1 = (-b + sqrt(b * b - 4 * a * c)) / 2 * a
            x2 = (-b - sqrt(b * b - 4 * a * c)) / 2 * a
            result_message = f'Квадратное уравнение имеет два действительных корня: ' \
                      f'x1 = {round(x1, ndigits=1)}, x2 = {round(x2, ndigits=1)}'

        context.update({'d': d, 'result_message': result_message})
    return render(request, 'quadratic/results.html', context)

