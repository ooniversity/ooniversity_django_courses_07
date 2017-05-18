from django.shortcuts import render


def quadratic_results(request):

	values = {}
	messages = {}

	for arg in request.GET:
	
		try:
			values[arg] = int(request.GET[arg])
		except ValueError:
			if not request.GET[arg]:
				messages[arg] = 'коэффициент не определен'
			elif not request.GET[arg].replace('-','').isdigit():
				messages[arg] = 'коэффициент не целое число'

			values[arg] = request.GET[arg]

	if 'a' in values and values['a'] == 0:
		messages['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'

	print(request.GET['a'])

	if len(messages) == 0:
		desc = values['b']**2 - 4*values['a']*values['c']
		values['desc'] = 'Дискриминант: ' + str(desc)

		if desc < 0:

			result = 'Дискриминант меньше нуля, квадратное уравнение \
			не имеет действительных решений.'

		elif desc == 0:

			x = -values['b']/2*values['a']
			result = 'Дискриминант равен нулю, квадратное уравнение имеет \
			один действительный корень: x1 = x2 = ' + str(x)

		elif desc > 0:

			x1 = (-values['b'] + desc**0.5)/2*values['a']
			x2 = (-values['b'] - desc**0.5)/2*values['a']
			result = 'Квадратное уравнение имеет два действительных \
			корня: x1 = {0}, x2 = {1}'.format(x1, x2)

		messages['result'] = result

	context = {'values': values, 'messages': messages}

	return render(request, 'result.html', context)