from django.shortcuts import render, redirect, reverse, get_object_or_404
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class StudentDetailView(DetailView):
    model = Student

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        messages.success(self.request, 'Студент {} {} успешно добавлен.'.format(data['name'], data['surname']))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def delete(self, request, *args, **kwargs):
        pk = self.get_object().id
        data = Student.objects.get(id=pk)
        print(data)
        messages.success(self.request, 'Info on {} {} has been successfully deleted.'.format(data.name, data.surname))
        response = super().delete(self, request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        pk = self.get_object().id
        context = super().get_context_data(**kwargs)
        context['remove_student'] = Student.objects.get(id=pk)
        context['title'] = 'Student info suppression'
        return context
