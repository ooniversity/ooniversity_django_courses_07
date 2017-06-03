from django.shortcuts import render


def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    q_dict = {'a1': a, 'b1': b, 'c1': c}
    
    try:
        a = int(a)
    except ValueError:
        q_dict["outa"] = "коэффициент не целое число"
    if a == '':
        q_dict["outa"] = "коэффициент не определен"
    if a == 0:
        q_dict["outa"] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    
    try:
        b = int(b)
    except ValueError:
        q_dict["outb"] = "коэффициент не целое число"
    if b == '':
        q_dict["outb"] = "коэффициент не определен"
    
    try:
        c = int(c)
    except ValueError:
        q_dict["outc"] = "коэффициент не целое число"
    if c == '':
        q_dict["outc"] = "коэффициент не определен"
    if type(a) == int and type(b) == int and type(c) == int and a != 0:
        d = b ** 2 - 4 * a * c
        q_dict["discriminant"] = "Дискриминант: %d" %(d)
        if d == 0:
            x1 = -b / (2 * a)
            q_dict["one_param"] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x1)
        elif d > 0:
            x1 = (-b + (d ** 0.5)) / (2 * a)
            x2 = (-b - (d ** 0.5)) / (2 * a)
            print(x1)
            q_dict["two_param"] = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)
        elif d < 0:
            q_dict["no_param"] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    return render(request, "quadratic/results.html", q_dict)
