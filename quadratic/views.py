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
    
    return render(request, "results.html", q_dict)



