from django.shortcuts import render
from math import sqrt
from .forms import QuadraticForm

  

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


def quadratic_results(request):
    
    form = QuadraticForm()
    
    if 0 == 0:

        mess_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

        context = {'mess_a':mess_a, 'form':form}
    
    else:
    
        q = quadratic(form.a, form.b, form.c)
    
        context = {'mess_a':mess_a, 'mes_discr':q[0], 'mes':q[1], 'form':form}

    return render(request, "results.html", context)
