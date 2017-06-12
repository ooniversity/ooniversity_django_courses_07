# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Student
from .forms import StudentModelForm


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'  # to avoid ImproperlyConfigured error
    # form_class = StudentModelForm
    # form = StudentModelForm  # to avoid ImproperlyConfigured error
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been successfully added.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)

    # def form_valid(self, form):
    #     super_valid = super(StudentCreateView, self).form_valid(form)
    #     messages.success(self.request,
    #                      'Student {} {} has been successfully added.'.format(self.object.name, self.object.surname))
    #     return super_valid
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StudentCreateView, self).get_context_data(**kwargs)
    #     context.update({
    #         "title": 'New student'
    #     })
    #     return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'  # to avoid ImproperlyConfigured error
    # form_class = StudentModelForm
    # form = StudentModelForm  # to avoid ImproperlyConfigured error
    success_url = reverse_lazy('students:list_view')
    # success_url = '/students/edit/%(id)d/'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    # def form_valid(self, form):
    #     messages.success(self.request, 'Info on the student has been successfully changed.')
    #     return super(StudentUpdateView, self).form_valid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StudentUpdateView, self).get_context_data(**kwargs)
    #     context.update({
    #         "title": 'Edit student data'
    #     })
    #     return context


class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'  # to avoid ImproperlyConfigured error
    # form_class = StudentModelForm
    # form = StudentModelForm  # to avoid ImproperlyConfigured error
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Info on %s %s has been successfully deleted.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     delete_super = super(StudentDeleteView, self).delete(request, *args, **kwargs)
    #     messages.success(self.request,
    #                      'Info on {} {} has been successfully deleted.'.
    #                      format(self.object.name, self.object.surname))
    #     return delete_super
