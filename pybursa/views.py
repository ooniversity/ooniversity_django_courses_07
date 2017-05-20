from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')

