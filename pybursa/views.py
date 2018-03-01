from django.views import generic
from courses.models import Course

class IndexView(generic.ListView):
    model = Course
    template_name = 'index.html'
