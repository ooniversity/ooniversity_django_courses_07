from django.shortcuts import render

def index(request):
    print(request)
    return render(request, 'index.html')
    
def contact(request):
    print(request)
    return render(request, 'contact.html')

def student_detail(request):
    print(request)
    return render(request, 'student_detail.html')

def student_list(request):
    print(request)
    return render(request, 'student_list.html')
