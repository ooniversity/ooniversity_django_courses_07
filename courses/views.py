from courses.models import Course, Lesson
from courses.forms import LessonModelForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(generic.DetailView):
    logger.debug('Courses detail view has been debugged!')
    logger.info('Logger of courses detail view informs you!')
    logger.warning('Logger of courses detail view warns you!')
    logger.error('Courses detail view went wrong!')

    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


class CourseCreateView(SuccessMessageMixin, generic.CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('index')
    success_message = 'Course %(name)s has been successfully added.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

class CourseUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'form'
    success_message = 'The changes have been saved.'

    def get_success_url(self):
        return reverse('courses:edit', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

class CourseDeleteView(generic.DeleteView):
    model = Course
    fields = '__all__'
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    success_message = 'Course %s has been deleted.'

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['pk'])
        messages.success(self.request, self.success_message % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

class LessonCreateView(SuccessMessageMixin, generic.CreateView):
    model = Lesson
    fields = '__all__'
    template_name = 'courses/add_lesson.html'
    success_message = 'Lesson %(subject)s has been successfully added.'    
    
    def get_success_url(self):
        return reverse('courses:detail', args=[self.get_object().id])

    def get_initial(self):
        initial = super().get_initial()
        initial['course'] = self.kwargs['pk']
        return initial
