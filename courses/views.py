from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson
from coaches.models import Coach
from django.views import generic

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

    # def get_queryset(self):
    #     self.course = get_object_or_404(Course, name=self.args[0])
    #     return Lesson.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list']= Lesson.objects.all().filter(course = self.object)
        context['assistant_list']= Coach.objects.all().filter(assistant_courses = self.object)
        context['coach_list']= Coach.objects.all().filter(coach_courses = self.object)
        return context
