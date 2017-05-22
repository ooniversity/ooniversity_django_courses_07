from django.shortcuts import render
from django.http import HttpResponse
from quadratic.quadratic_handler import QuadraticEducation
# Create your views here.



def chck_params(parametr):
    check_parametr = False
    # try:
    #     parametr = int(parametr)
    # except:
    #     check_parametr = False
    if ((parametr.isdigit()==True)or ((len(parametr)>1)and(parametr[0]=='-')and(parametr[1:].isdigit())==True)):
         check_parametr = True
    return check_parametr

def quadratic_results(request):
    a = ''
    b = ''
    c = ''
    d = ''
    x1 =''
    x2 =''
    context = {}
    checker = True
    template =  'results.html'
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    print(a,b,c)
    if (a == '0' or a=='' or b == '' or c == '' ):
        checker = False
        context = {"a": a,"b": b,"c": c,"check_a": chck_params(a),"check_b": chck_params(b),"check_c": chck_params(b),"checker": checker}
        return render(request,(template),context)
    elif(chck_params(a)==False or chck_params(b)==False or chck_params(c)==False):
        checker = False
        context = {"a": a, "b": b, "c": c, "check_a": chck_params(a), "check_b": chck_params(b),   "check_c": chck_params(b),"checker": checker}
        return render(request, (template), context)
    else:
        qe = QuadraticEducation(int(a),int(b),int(c))

        qe.calc_descr()
        d = qe.get_descr()
        print(d)
        x1 = str(qe.calc_root())
        x2 = qe.calc_root(order=2)
        print(x1,x2)
	context = {"a":a,"b":b,"c":c,"check_a":chck_params(a),"check_b":chck_params(b),"check_c":chck_params(b),"discr":d,"x1":x1,"x2":x2,"checker": checker}
    return render(request,(template),context)
