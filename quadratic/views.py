from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuadraticForm
import math


def solve(a, b, c, d):
	if d == 0:
		x1 = x2 = (-b + math.sqrt(b ** 2 - 4 * a * c))/ (2 * a)    	
	else:
		x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
		x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
	return x1, x2

def descr(a, b, c):
	return b ** 2 - 4 * a * c
		
def check(param):
	try:
		param = int(param)
	except ValueError:
		return False
	return True
    
def quadratic_results(request):
    my_dict = {}
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            my_dict = form.cleaned_data
            my_dict['form'] = form
            my_dict['next'] = True
            my_dict['d'] = descr(my_dict['a'], my_dict['b'], my_dict['c'])
            if my_dict['d'] >= 0:
                my_dict['x1'], my_dict['x2'] = solve(my_dict['a'], my_dict['b'], my_dict['c'], my_dict['d'])
        else:
            my_dict['form'] = form
    else:
        form = QuadraticForm()
        my_dict['form'] = form             
    return render(request, 'results.html', my_dict)
