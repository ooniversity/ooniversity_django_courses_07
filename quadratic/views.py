from django.shortcuts import render


def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    dict_quadratic = dict(zip(["a1", "b1", "c1"], [a, b, c]))
    try:
        a = int(a)
    except ValueError:
        dict_quadratic["resA"] = "коэффициент не целое число"
    if a == '':
        dict_quadratic["resA"] = "коэффициент не определён"
    if a == 0:
        dict_quadratic["resA"] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    try:
        b = int(b)
    except ValueError:
        dict_quadratic["resB"] = "коэффициент не целое число"
    if b == '':
        dict_quadratic["resB"] = "коэффициент не определён"
    try:
        c = int(c)
    except ValueError:
        dict_quadratic["resC"] = "коэффициент не целое число"
    if c == '':
        dict_quadratic["resC"] = "коэффициент не определён"
    if type(a) == int and type(b) == int and type(c) == int:
        d = b ** 2 - 4 * a * c
        dict_quadratic["discriminant"] = "Дискриминант: %d" %(d)
        if d > 0:
            x1 = (-b + (d ** 0.5)) / (2 * a)
            x2 = (-b - (d ** 0.5)) / (2 * a)
            print(x1)
            dict_quadratic["two_x"] = "Квадратное уравнение имеет два действительных корня: x1 = %d, x2 = %d" %(x1, x2)
        elif d == 0:
            x1 = -b / (2 * a)
            dict_quadratic["one_x"] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %d" %(x1)
        elif d < 0:
            dict_quadratic["not_x"] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    return render(request, "results.html", dict_quadratic)



