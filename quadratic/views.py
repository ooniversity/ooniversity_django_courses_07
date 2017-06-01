from django.shortcuts import render
import math
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
    else:
        form = QuadraticForm()
    context = {'form': form}
    if form.is_valid():
        print('Valid')
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        c = int(request.GET['c'])
        D = b ** 2 - 4 * a * c
        context['D'] = D
        if context['D'] < 0:
            context['message_d'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif context['D'] == 0:
            x = -b / 2 * a
            context['message_d'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный " \
                                   "корень: x1 = x2 = " + str(x)
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            context['message_d'] = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, " \
                                   "x2 = %.1f" % (x1, x2)

    return render(request, 'quadratic/results.html', context=context)
