from django.shortcuts import render
from courses.models import Course

def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
