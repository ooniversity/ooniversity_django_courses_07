from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

from courses.models import Course

#from django.template import RequestContext, loader
#from .models import Choice, Question

def index(request):
    course_list = Course.objects.all()
    return render(request, 'index.html', {'course_list': course_list})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')