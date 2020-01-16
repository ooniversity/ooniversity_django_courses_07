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
            message = f'Квадратное уравнение имеет два действительных корня: ' \
                      f'x1 = {round(x1, ndigits=1)}, x2 = {round(x2, ndigits=1)}'

        context.update({'d': d, 'result_message': result_message})
    return render(request, 'results.html', context)

#     for key in arg_list:
#         context.update(arg_validate(data, key))
#
#     if data['a'] == '0':
#         context['a_error'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
#
#     if not any('error' in key for key in context.keys()):
#         context.update(root_equation(context))
# else:
#     context = dict.fromkeys(['a_error', 'b_error', 'c_error'], 'коэффициент не определен')
#
# return render(request, 'results.html', context)

# def is_integer(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False
#
#
# def arg_validate(data, key: str):
#     arg = data.get(f'{key}')
#     result = {key: arg}
#     if arg:
#         if is_integer(arg):
#             result[key] = int(arg)
#         else:
#             result[f'{key}_error'] = 'коэффициент не целое число'
#     else:
#         result[f'{key}_error'] = 'коэффициент не определен'
#     return result
#
#
# def root_equation(content):
#     a = content.get('a')
#     b = content.get('b')
#     c = content.get('c')
#     if a and b and c:
#         discriminant = b * b - 4 * a * c
#
#         if discriminant == 0:
#             x = - b / 2 * a
#             message = f'Дискриминант равен нулю, квадратное уравнение ' \
#                       f'имеет один действительный корень: x1 = x2 = {x}'
#
#         elif discriminant > 0:
#             x1 = (-b + sqrt(b * b - 4 * a * c)) / 2 * a
#             x2 = (-b - sqrt(b * b - 4 * a * c)) / 2 * a
#             message = f'Квадратное уравнение имеет два действительных корня: ' \
#                       f'x1 = {round(x1, ndigits=1)}, x2 = {round(x2, ndigits=1)}'
#
#         else:
#             message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
#         return {'discriminant': discriminant, 'message': message}
#     return {}
