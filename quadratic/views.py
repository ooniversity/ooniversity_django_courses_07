from django.shortcuts import render


def quadratic_results(request):
    #get arguments
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    parameters_dict = {"a": a, "b": b, "c": c}
    #test arguments type
    try:
        a = int(a)
        if a == 0:
            parameters_dict.update({"a_add": "коэффициент при первом слагаемом не может быть равен нулю"})
    except:
        if a == '':
            parameters_dict.update({"a_add": "коэффициент не определен"})
        else:
            parameters_dict.update({"a_add": "коэффициент не целое число"})
    try:
        b = int(b)
    except:
        if b == '':
            parameters_dict.update({"b_add": "коэффициент не определен"})
        else:
            parameters_dict.update({"b_add": "коэффициент не целое число"})
    try:
        c = int(c)
    except:
        if c == '':
            parameters_dict.update({"c_add": "коэффициент не определен"})
        else:
            parameters_dict.update({"c_add": "коэффициент не целое число"})
    #calculation of roots
    if len(parameters_dict) == 3:
        D = int(b)**2-4*int(a)*int(c)
        parameters_dict.update({"discriminant": 'Дискриминант: ' + str(D)})
        if D < 0:
            parameters_dict.update({"discriminant_add": "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."})
        elif D == 0:
            x = -1*int(b)/2
            parameters_dict.update({"roots": "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = " + str(x)})
        else:
            x1 = (-1*int(b) + D**0.5)/2
            x2 = (-1*int(b) - D**0.5)/2
            parameters_dict.update({"roots": "Квадратное уравнение имеет два действительных корня: x1 = " + str(x1) + " x2 = " + str(x2)})
    return render(request, "results.html", parameters_dict)
