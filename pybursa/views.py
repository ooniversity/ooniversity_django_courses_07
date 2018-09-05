from django.shortcuts import render
from courses.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses': courses})

def contact(request):
    return render(request, "contact.html")

