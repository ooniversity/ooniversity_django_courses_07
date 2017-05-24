from django.shortcuts import render
from courses.models import Course


def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')