from django.shortcuts import render


def coeff_type(p):
    try:
        p = int(p)
        p_note = True        
    except ValueError:
        p_note = False
    return p_note

def discriminant(a, b, c):
    d = b**2-4*a*c    
    return d

def quadratic_roots(a, b, c, d):
    x1 = (-b+d**(1/2))/2*a    
    x2 = (-b-d**(1/2))/2*a
    return x1, x2

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    context = {'a':a, 'b':b, 'c':c}    
    a_note = coeff_type(a)
    b_note = coeff_type(b)
    c_note = coeff_type(c)
    context.update({'a_note':a_note, 'b_note':b_note, 'c_note':c_note})
    
    if a_note and b_note and c_note and a != '0':
        d = discriminant(int(a),int(b),int(c))
        context['d'] = d
        if d >= 0:
            x1,x2 = quadratic_roots(int(a),int(b),int(c),d)
            context['x1'] = round(x1, 1)
            context['x2'] = round(x2, 1)
    print(context) 
    return render(request, 'results.html', context)

# Create your views here.
