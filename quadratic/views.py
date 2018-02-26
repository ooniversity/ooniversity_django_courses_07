from django.shortcuts import render
from quadratic.forms import QuadraticForm

def quadratic_results(request):    
    errord = ''
    discr = ''
    d, x1, x2 = 0, 0, 0
    
    if request.GET == {}:
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.GET)
    
    if form.is_valid():
        a = request.GET['a']    
        b = request.GET['b']    
        c = request.GET['c']
        d = int(b)**2 - 4*int(a)*int(c)
        discr = 'Дискриминант: %d' % d
        
        if d >= 0:
            x1 = round((-int(b) + (d**0.5)) / 2*int(a), 1)
            x2 = round((-int(b) - (d**0.5)) / 2*int(a), 1)

        if d < 0:
            errord = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif d == 0:
            errord = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x1
        elif d > 0:
            errord = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (x1, x2)           
    return render(request, 'quadratic/results.html', context = {'errord': errord,
                                                                'discr': discr,
                                                                'form': form})
