from django.shortcuts import render
from math import sqrt
from quadratic.forms import QuadraticForm
from quadratic.quadratic import QuadraticEquation
#Инт в стринг с исключениями и переопределениям для квадротного уравнения
def int_to_str(num):
    flag=True
    code=None
    if num==None or num=='':
        code="коэффициент не определен"
        flag=False
    else:
        try:
            num = int(num)
        except ValueError:
            code='коэффициент не целое число'
            flag = False
    if num==None:
        num = ''
    return num,flag,code

#Квадратное уравнения вьюха
def quadratic_results(request):
    if request.GET == {}:
        form = QuadraticForm()
        context = {'form': form}
    else:
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            result = QuadraticEquation(**form.cleaned_data)
            result.solve()
            context['result'] = result
    return render(request, 'quadratic/results.html', context)