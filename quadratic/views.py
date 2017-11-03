from django.shortcuts import render
from .forms import QuadraticForm
import math

# Create your views here.
def quadratic_results(request):
    form = QuadraticForm()
    if request.GET:
            form = QuadraticForm(request.GET)
        
    context = {'form': form}
                
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        d = b**2 - 4*a*c
        context['d'] = 'Дискриминант: {}'.format(d)
         
        if d < 0:
            context['result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            x = -b / 2*a
            context['result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
        elif d > 0:
            x1 = (-b + math.sqrt(d)) / 2*a
            x2 = (-b - math.sqrt(d)) / 2*a
            context['result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)         
    
    return render(request, 'quadratic/results.html', context)