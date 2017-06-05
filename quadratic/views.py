from django.shortcuts import render, redirect
from .forms import QuadraticForm



def discriminant(a, b, c):
    d = b**2-4*a*c    
    return d

def quadratic_roots(a, b, d):
    x1 = (-b+d**(1/2))/2*a    
    x2 = (-b-d**(1/2))/2*a
    return round(x1, 1), round(x2, 1)



def quadratic_results(request):
     # if this is a POST request we need to process the form data
    if request.POST:
        # create a form instance and populate it with data from the request:
        form = QuadraticForm(request.POST)
        print (request.POST)
        print (form)
        # check whether it's valid:
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            context['form'] = form.cleaned_data
            print (form.cleaned_data)
            d = discriminant(a, b, c)
            context['d'] = d
            if d < 0:
                result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif d == 0:
                x1,x2 = quadratic_roots(a, b, d)
                context['x1'] = x1
                context['x2'] = x2
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
            else:
                x1,x2 = quadratic_roots(a, b, d)
                context['x1'] = x1
                context['x2'] = x2
                result_message = "Квадратное уравнение имеет два действительных корня: x1 = -5.0, x2 = 7.0" 

            context['result_message'] = result_message
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('results')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuadraticForm()
        return render(request, 'quadratic/results.html', {'form': form})

    # Create your views here.
