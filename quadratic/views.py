from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):    
    calc_data = {}

    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']    
            b = form.cleaned_data['b']    
            c = form.cleaned_data['c']
            calc_data['d'] = b**2 - 4*a*c
            if calc_data['d'] >= 0:
                calc_data['x1'] = (-b + (calc_data['d']**0.5)) / 2*a
                calc_data['x2'] = (-b - (calc_data['d']**0.5)) / 2*a        
    else:
        form = QuadraticForm()
    
    return render(request, 'quadratic/results.html', context = {'calc_data': calc_data,
                                                                'form': form})
