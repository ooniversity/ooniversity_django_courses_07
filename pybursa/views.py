from django.shortcuts import render
from courses.models import Course
from django.views import generic

def index(request):
    courses = Course.objects.all()
    context = {'courses_list': courses, }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

# class ContatView(generic.ListView):
#     template_name = 'contact.html'

