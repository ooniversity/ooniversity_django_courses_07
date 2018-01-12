from django.shortcuts import render

def quadratic_results(request):
    if request.method == 'GET':
        param = request.GET
        context = {'a': param.get('a'), 'b': param.get('b'), 'c': param.get('c'), }
        context = calculate(context)
        return render(request, "results.html", context)


def calculate(context):
    data = context
    param = {}
    for key in data.keys():
        if data[key] is None or data[key] == '':
            data[key] = 'коэффициент не определен'
        elif data[key].isdigit():
            param[key] = int(data[key])
        elif data[key][0] == '-' and data[key][1:].isdigit():
            param[key] = int(data[key])
        else:
            data[key] += ' коэффициент не целое число'

    if data[key].isdigit() and int(data['a']) ==  0:
        data['a'] = '0 коэффициент при первом слагаемом уравнения не может быть равным нулю'
        return data
    if len(param) != 3:
        return data

    d = (param['b'] ** 2) - (4 * param['a'] * param['c'])
    if d < 0:
        data['disk'] = 'Дискриминант: {} Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений. '.format(d)
    elif d == 0:
        sol1 = (-param['b'] - d ** 0.5) / (2 * param['a'])
        data['disk'] = 'Дискриминант: {} Дискриминант равен нулю, ' \
                                              'квадратное уравнение имеет один ' \
                                              'действительный корень: x1 = x2 = {}'.format(d, sol1)
    else:
        sol1 = (-param['b'] - d ** 0.5) / (2 * param['a'])
        sol2 = (-param['b'] + d ** 0.5) / (2 * param['a'])
        data['disk'] = 'Дискриминант: {} Квадратное уравнение ' \
                       'имеет два действительных корня: x1 = {}, x2 = {}'.format(d, sol2, sol1)

    return data
