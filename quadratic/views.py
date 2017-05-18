from django.shortcuts import render


def quadratic_results(request):

	params = {}
	errors = {}

	for arg in request.GET:
	
		try:
			params[arg] = int(request.GET[arg].strip())
		except ValueError:
			if not request.GET[arg]:
				errors[arg] = 'коэффициент не определен'
			elif not request.GET[arg].replace('-','').isdigit():
				errors[arg] = 'коэффициент не целое число'

	if request.GET['a'] == '0':
		errors['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

	params['errors'] = errors

	if not len(errors):
		params['desc'] = params['b']**2 - 4*params['a']*params['c']

		if params['desc'] < 0:

			result = 'Дискриминант меньше нуля, квадратное уравнение \
			не имеет действительных решений.'

		elif params['desc'] == 0:

			x = -params['b']/2*params['a']
			result = 'Дискриминант равен нулю, квадратное уравнение имеет \
			один действительный корень: x1 = x2 = ' + str(x)

		elif params['desc'] > 0:

			x1 = (-params['b'] + params['desc']**0.5)/2*params['a']
			x2 = (-params['b'] - params['desc']**0.5)/2*params['a']
			result = 'Квадратное уравнение имеет два действительных \
			корня: x1 = {0}, x2 = {1}'.format(x1, x2)

		params['result'] = result
	

	return render(request, 'result.html', params)