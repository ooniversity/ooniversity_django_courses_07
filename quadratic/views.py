from django.shortcuts import render
from .forms import QuadraticForm

def quadratic_results(request):
    form = QuadraticForm()
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    context = {"a": a, "b": b, "c": c}
    context['form'] = form
    try:
        a = int(a)
        if a == 0:
            context["a_add"] = "коэффициент при первом слагаемом не может быть равен нулю"
    except:
        if a == '':
            context["a_add"] = "коэффициент не определен"
        else:
            context["a_add"] = "коэффициент не целое число"
    try:
        b = int(b)
    except:
        if b == '':
            context["b_add"] = "коэффициент не определен"
        else:
            context["b_add"] = "коэффициент не целое число"
    try:
        c = int(c)
    except:
        if c == '':
            context["c_add"] = "коэффициент не определен"
        else:
            context["c_add"] = "коэффициент не целое число"
    if len(context) == 4:
        D = int(b)**2-4*int(a)*int(c)
        context["discriminant"] = "Дискриминант: " + str(D)
        if D < 0:
            context["discriminant_add"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif D == 0:
            x = -1*int(b)/(2*a)
            context["roots"] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = " + str(x)
        else:
            x1 = (-1*int(b) + D**0.5)/(2*a)
            x2 = (-1*int(b) - D**0.5)/(2*a)
            context["roots"] = "Квадратное уравнение имеет два действительных корня: x1 = " + str(x1) + " x2 = " + str(x2)
    return render(request, "results.html", context)
