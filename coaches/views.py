from coaches.models import Coach
from courses.models import Course
from django.views import generic

class DetailView(generic.DetailView):
    model = Coach
    template_name = 'coaches/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assistant_list']= Coach.objects.all().filter(assistant_courses = self.object)
        context['coach_list']= Coach.objects.all().filter(coach_courses = self.object)
        return context

