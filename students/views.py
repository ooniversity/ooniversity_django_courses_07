from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        students = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = students.filter(courses=course_id)
        return students


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        fullname = form.instance.name + ' ' + form.instance.surname
        messages.success(self.request, 'Student %s has been successfully added.' % fullname)
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get('pk'))
        messages.success(self.request, 'Info on %s has been successfully deleted.' % student)
        return super().delete(self, request, *args, **kwargs)