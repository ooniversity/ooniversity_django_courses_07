from django.shortcuts import render
from courses.models import Course
from django.views import generic

def contact(request):
    return render(request, 'contact.html')

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'qs_list'
    
    def get_queryset(self):
        return Course.objects.all()
