from django.shortcuts import render
import math

# Create your views here.
def quadratic_results(request):
    errors = {}
    x1 = x2 = d = None
    
    get = request.GET.dict()
    
    for param in get:
        if not get[param]:
            errors[param] = 'коэффициент не определен'
        else:
            try:
                get[param] = int(get[param])
                
                if get['a'] == 0:
                    errors['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
            except:
                errors[param] = 'коэффициент не целое число'
                
                
    if not errors:
        d = get['b']**2 - 4*get['a']*get['c']
        
        if d == 0:
            x1 = x2 = -get['b'] / 2*get['a']
        elif d > 0:
            x1 = (-get['b'] + math.sqrt(d)) / 2*get['a']
            x2 = (-get['b'] - math.sqrt(d)) / 2*get['a']
            
    
    return render(request, 'results.html', {
                                            'errors': errors, 
                                            'get': get,
                                            'd': d,
                                            'x1': x1,
                                            'x2': x2
                                            })