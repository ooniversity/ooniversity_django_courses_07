from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from students.models import Student
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2    

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id != None and course_id.isnumeric():
            qs = qs.filter(courses__id=course_id)
        return qs
        

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student %s %s has been successfully added.' % (form.cleaned_data['name'], form.cleaned_data['surname']))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        context['operation_type_name'] = 'Создание нового студента'
        context['button_name'] = 'Сохранить'
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
        context['operation_type_name'] = 'Редактирование данных студента'
        context['button_name'] = 'Изменить'
        return context
    
    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.kwargs.get('pk')})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(request, 'Student %s %s has been successfully deleted.' % (self.object.name, self.object.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
