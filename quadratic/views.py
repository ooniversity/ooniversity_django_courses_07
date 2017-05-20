from django.shortcuts import render
from django.http import HttpResponse
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
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	my_dict = {'a': a, 'b': b, 'c': c}
	my_dict['a_norm'] = check(a)
	my_dict['b_norm'] = check(b)
	my_dict['c_norm'] = check(c)
	if my_dict['a_norm'] and my_dict['b_norm'] and my_dict['c_norm'] and a != '0':
		my_dict['next'] = True
		my_dict['d'] = descr(int(a), int(b), int(c))
		if my_dict['d'] >= 0:
			my_dict['x1'], my_dict['x2'] = solve(int(a), int(b), int(c), my_dict['d'])
	
	return render(request, 'results.html', my_dict)
