from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
