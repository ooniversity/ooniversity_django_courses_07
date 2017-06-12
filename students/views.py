from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
    

class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student %s %s has been successfully added." % (form.instance.name, form.instance.surname))
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Info has been successfully deleted.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

