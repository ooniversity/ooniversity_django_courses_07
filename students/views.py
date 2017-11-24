from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
# Create your views here.


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            return qs.filter(courses__id = course_id)
        else:
            return qs
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Список студентов'
        return context
        
        
class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Информация о студенте'
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student has been successfully added.")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student registration'
        return context
        
        
class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student has been successfully updated")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info update'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info suppression'
        return context  
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Info on student has been successfully deleted.")
        return response
        

