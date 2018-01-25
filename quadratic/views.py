from django.shortcuts import render, redirect
from quadratic.forms import QuadraticForm
from django.http import HttpResponseRedirect


def quadratic_results(request):
    form = QuadraticForm(label_suffix='')
    if request.method == 'GET':
        form = QuadraticForm(request.GET, label_suffix='', )
    context = {'form': form}
    if form.is_valid():
            data = form.cleaned_data
            context['result'] = calculate(data)

    return render(request, "results.html", context)


def calculate(data):
    # data = context
    # param = {}
    # for key in data.keys():
    #     if data[key] is None or data[key] == '':
    #         data[key] = 'коэффициент не определен'
    #     elif data[key].isdigit():
    #         param[key] = int(data[key])
    #     elif data[key][0] == '-' and data[key][1:].isdigit():
    #         param[key] = int(data[key])
    #     else:
    #         data[key] += ' коэффициент не целое число'

    # if data[key].isdigit() and int(data['a']) == 0:
    #     data['a'] = '0 коэффициент при первом слагаемом уравнения не может быть равным нулю'
    #     return data
    # if len(param) != 3:
    #     return data
    a = data['a']
    b = data['b']
    c = data['c']

    d = (b ** 2) - (4 * a * c)
    result = ''
    if d < 0:
        result = 'Дискриминант: {} Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений. '.format(
            d)
    elif d == 0:
        sol1 = (-b - d ** 0.5) / (2 * a)
        result = 'Дискриминант: {} Дискриминант равен нулю, ' \
                       'квадратное уравнение имеет один ' \
                       'действительный корень: x1 = x2 = {}'.format(d, sol1)
    else:
        sol1 = (-b - d ** 0.5) / (2 * a)
        sol2 = (-b + d ** 0.5) / (2 * a)
        result = 'Дискриминант: {} Квадратное уравнение ' \
                       'имеет два действительных корня: x1 = {}, x2 = {}'.format(d, sol2, sol1)

    return result
