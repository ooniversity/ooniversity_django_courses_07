from django.shortcuts import render
from math import sqrt
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
    a,b,c=request.GET.get('a'),request.GET.get('b'),request.GET.get('c');
    a,f1,c1=int_to_str(a)
    if a == 0:
        c1 ='коэффициент при первом слагаемом уравнения не может быть равным нулю'
        flag=False
    b, f2,c2 = int_to_str(b)
    c, f3,c3 = int_to_str(c)
    flag=f1 and f2 and f3
    d = b*b-4*a*c if flag else None
    message = ''
    x1=x2=None
    if flag and d>=0:
        x1=(-1*b + sqrt(d)) / float(2*a)
        x2=(-1*b - sqrt(d)) / float(2*a)
    return render(request,'quadratic/results.html',{'a':a,'b':b,'c':c, 'D':d,'x1':x1,'x2':x2,
                                          'c1':c1,'c2':c2,'c3':c3})