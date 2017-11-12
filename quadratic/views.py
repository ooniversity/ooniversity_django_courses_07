from django.shortcuts import render
from math import sqrt


def test(par):
    
    if par == '':

        mes = 'коэффициент не определен'

        return mes

    try:

        int(par)

    except:

        mes = 'коэффициент не целое число'

        return mes
    

def quadratic(a,b,c):

    discr = b*b - 4 * a * c

    mes_discr = 'Дискриминант: ' + str(discr)

    if discr < 0:
           
        mes = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    
    if discr == 0:

        x = -b/(2*a)

        mes = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)

    if discr > 0:

        x1 = (-b + sqrt(discr)) / (2 * a)

        x2 = (-b - sqrt(discr)) / (2 * a)

        mes = 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)

    return [mes_discr, mes]


def results(request):
    
    vars = (request.GET)
    
    a, b, c = vars['a'], vars['b'], vars['c']     

    mess_a, mess_b, mess_c = test(a), test(b), test(c)

    if test(a) == None and int(a) == 0:

        mess_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

    context = {'a':a, 'b':b, 'c':c, 'mess_a':mess_a, 'mess_b':mess_b, 'mess_c':mess_c}
    
    if test(a) == None and test(b) == None and test(c) == None and int(a) != 0:
    
        q = quadratic(int(a), int(b), int(c))
    
        context = {'a':a, 'b':b, 'c':c, 'mess_a':mess_a, 'mess_b':mess_b, 'mess_c':mess_c, 'mes_discr':q[0], 'mes':q[1]}

    return render(request, "results.html", context)
