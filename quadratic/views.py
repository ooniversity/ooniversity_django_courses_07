from django.shortcuts import render, redirect
from .forms import QuadraticForm



def discriminant(a, b, c):
    d = b**2-4*a*c    
    return d

def quadratic_roots(a, b, d):
    x1 = (-b+d**(1/2))/(2*a)    
    x2 = (-b-d**(1/2))/(2*a)
    return x1,x2

def quadratic_results(request):
    form = QuadraticForm(request.GET)
    context = {'form':form}
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        d = discriminant(a, b, c)
        context.update({'d':'Дискриминант: {}'.format(d)})
        if d < 0:
            result_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            x1,x2 = quadratic_roots(a, b, d)            
            result_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x1)
        else:
            x1,x2 = quadratic_roots(a, b, d)           
            result_message = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)
        context.update({'result_message':result_message})
    return render(request, 'quadratic/results.html', context)

    # Create your views here.
