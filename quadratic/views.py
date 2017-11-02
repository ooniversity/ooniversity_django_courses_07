from django.shortcuts import render
from .forms import QuadraticForm
from django.forms import Form 
import math

# Create your views here.
def quadratic_results(request):
    get = request.GET.dict()
    x1 = x2 = None
    if get:
        form = QuadraticForm(request.GET)
    else:
        form = Form()
        
    context = {'error': False}
    context['form'] = form
                
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        d = b**2 - 4*a*c
         
        if d == 0:
            x1 = x2 = -b / 2*a
        elif d > 0:
            x1 = (-b + math.sqrt(d)) / 2*a
            x2 = (-b - math.sqrt(d)) / 2*a
            
        context['d'] = d
        context['x1'] = x1
        context['x2'] = x2
    else:
        context['error'] = True            
    
    return render(request, 'quadratic/results.html', context)