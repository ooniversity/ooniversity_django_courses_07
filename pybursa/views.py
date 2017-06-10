from django.shortcuts import render
from courses.models import Course

def index(request):
    course_list = Course.objects.all()
    return render(request, "index.html", {'course_list': course_list})

def contact(request):
    return render(request, "contact.html")
