from django.shortcuts import render
from courses.models import Course
from datetime import datetime, date

def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses_dict': [courses[i] for i in range(len(courses))]})

def contact(request):
    return render(request, "contact.html")

