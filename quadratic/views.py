from django.shortcuts import render, redirect
from .forms import QuadraticForm

def quadratic_results(request):
	context = {}
	if request.GET:
		form = QuadraticForm(request.GET)
		if form.is_valid():
			a = form.cleaned_data.get('a')
			b = form.cleaned_data.get('b')
			c = form.cleaned_data.get('c')
			desc = b**2 - 4*a*c
			context['desc'] = 'Дискриминант: %d' % desc
			if desc < 0:
				context['result'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			elif desc == 0:
				x = -b/(2*a)
				context['result'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
			elif desc > 0:
				x1 = (-b + desc**0.5)/(2*a)
				x2 = (-b - desc**0.5)/(2*a)
				context['result'] = 'Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}'.format(x1, x2)
	else:
		form = QuadraticForm()
	context['form'] = form
	return render(request, 'quadratic/results.html', context)