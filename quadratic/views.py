from django.shortcuts import render

def quadratic_results(request):
    sad_comment="коэффициент не определен"
    context={var:sad_comment for var in ['a','b','c']}
    for var,val in request.GET.items():
        try:
            answer=int(val)
            if var == 'a' and int(val)==0:
                answer="коэффициент при а не может быть равен нулю"
        except ValueError:
            if val =='': 
                answer=sad_comment
            else:
                answer="коэффициент не целое число"
        finally:
            context[var]=answer
    a=context['a']
    b=context['b']
    c=context['c']
    try:
        descr=b**2-4*a*c
        context['descr']="Дискриминант: {0}".format(descr)
        if descr==0:
            x_0=-b/(2*a)
            context['conclusion']="Квадратное уравнение имеет"\
                        " 1 действительный корень:x1=x2={0}".format(x_0)
        elif descr<0:
            context['conclusion']="Дискриминант меньше нуля. "\
                    "Уравнение не имеет действительных решений"
        elif descr>0:
            x_1=(-b+descr**0.5)/(2*a)
            x_2=(-b-descr**0.5)/(2*a)
            context['conclusion']="Уравнение имеет 2 действительных "\
            "корня: x1={0}, x2={1}".format(x_1,x_2)
    except TypeError:
        context['descr']=""
        context['conclusion']=""
    return render(request,'quadratic/results.html',context)
        
    
