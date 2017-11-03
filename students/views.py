from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from . import forms

# Create your views here.
class StudentListView(ListView):
    
    model = Student
    
    def get_queryset(self):
        get = self.request.GET.dict()
    
        if get and get['course_id']:
            return Student.objects.filter(courses__id=get['course_id']).all()
            
        return Student.objects.all()


    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        
        get = self.request.GET.dict()
        if get and get['course_id']:
            context['course_id'] = get['course_id']
            
        return context
    
    
class StudentDetailView(DetailView):
    
    model = Student


class StudentCreateView(CreateView):
    
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        
        return context
    
    
class StudentUpdateView(UpdateView):
    
    model = Student
    fields = '__all__'
    
    def get_success_url(self):
        return  reverse_lazy('students:update', kwargs={'student_id': self.object.id})
    
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        
        return context
    
    
class StudentDeleteView(DeleteView):
    
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        
        return context


# def create(request):
#     form = forms.StudentModelForm()
#     
#     if request.method == 'POST':
#         form = forms.StudentModelForm(request.POST)
#         
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student {} {} has been successfully added.'.format(form.cleaned_data['name'], form.cleaned_data['surname']))
#             
#             return redirect('students:list_view')
#     
#     return render(request, 'students/add.html', {'form': form})


# def edit(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     form = forms.StudentModelForm(instance=student)
#     
#     if request.method == 'POST':
#         form = forms.StudentModelForm(request.POST, instance=student)
#         
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Info on the student has been successfully changed.')
#             
#             return redirect('students:update', student_id=student.id)
# 
#     return render(request, 'students/edit.html', {'form': form})
    
    
# def remove(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     
#     if request.method == 'POST':
#         student.delete()
#         messages.success(request, 'Info on {} {} has been successfully deleted.'.format(student.name, student.surname))
#         
#         return redirect('students:list_view')
#     
#     return render(request, 'students/remove.html', {'student': student})
    