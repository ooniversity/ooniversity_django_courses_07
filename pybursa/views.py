from django.shortcuts import render

def index(request):
    return render(request, 'pybursa/index.html')
    
def contact(request):
    return render(request, 'pybursa/contact.html')

def student_detail(request):
    return render(request, 'pybursa/student_detail.html')

def student_list(request):
    return render(request, 'pybursa/student_list.html')
