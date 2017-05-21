from django.shortcuts import render
import math

def quadratic_results(request):
    message_a = message_b = message_c = message_d = ""
    try:
        a = int(request.GET['a'])
    except ValueError:
        a = request.GET['a']
        message_a = "коэффициент не целое число"
    try:
        b = int(request.GET['b'])
    except ValueError:
        b = request.GET['b']
        message_b = "коэффициент не целое число"
    try:
        c = int(request.GET['c'])
    except ValueError:
        c = request.GET['c']
        message_c = "коэффициент не целое число"

    if a == 0:
        message_a = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
    elif not a:
        message_a = "коэффициент не определен"
    if (not b) and (b !=0):
        message_b = "коэффициент не определен"
    if (not c) and (c != 0):
        message_c = "коэффициент не определен"
    context = {'a': a,
               'b': b,
               'c': c,
               'message_a': message_a,
               'message_b': message_b,
               'message_c': message_c,
               }
    if (message_a == "") and (message_b  == "") and (message_c == ""):
        D = b ** 2 - 4 * a * c
        context['D'] = D
        if context['D'] < 0:
            context['message_d'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif context['D'] == 0:
            x = -b / 2 * a
            context['message_d'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = " + str(x)
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            context['message_d'] = "Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f" % (x1, x2)

    return render(request, 'results.html', context=context)