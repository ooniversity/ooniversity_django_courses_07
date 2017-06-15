from django.contrib import messages
from .models import Student
from .forms import StudentModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import logging

logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        logger.debug('Students detail view has been debugged!')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id != None and course_id.isnumeric():
            qs = Student.objects.filter(courses__id__exact=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged!')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student %s has been successfully added.' % (self.object.fullname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self):
        return reverse_lazy('students:edit', kwargs={'pk': self.kwargs.get('pk')})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(request, "Info on %s has been successfully deleted." % (self.object.fullname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
