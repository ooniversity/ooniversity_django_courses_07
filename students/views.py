from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from . import forms
import logging

logger = logging.getLogger('students')

# Create your views here.
class StudentListView(ListView):
    
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        get = self.request.GET.dict()
    
        if get and 'course_id' in list(get.keys()):
            qs = qs.filter(courses__id=get['course_id'])
            
        return qs


    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        
        get = self.request.GET.dict()
        if get and 'course_id' in list(get.keys()):
            context['course_id'] = get['course_id']
            
        logger.debug('Students detail view has been debugged!')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
            
        return context
    
    
class StudentDetailView(DetailView):
    
    model = Student
    
    def get_queryset(self):
        return super(StudentDetailView, self).get_queryset()
    
    
    def get_context_data(self, **kwargs):
        return super(StudentDetailView, self).get_context_data(**kwargs)


class StudentCreateView(CreateView):
    
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        
        return context
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Student {} {} has been successfully added.'.format(form.cleaned_data['name'], form.cleaned_data['surname']))
        
        return super().form_valid(form)
    
    
class StudentUpdateView(UpdateView):
    
    model = Student
    fields = '__all__' 
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        
        return context
    
    
    def get_success_url(self):
        return reverse_lazy('students:update', args=[self.object.id])
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        
        return super().form_valid(form)
    
    
class StudentDeleteView(DeleteView):
    
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        
        return context
    
    
    def delete(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs['pk'])
        messages.success(self.request, 'Info on {} {} has been successfully deleted.'.format(student.name, student.surname))
        
        return super().delete(request, *args, **kwargs)
    