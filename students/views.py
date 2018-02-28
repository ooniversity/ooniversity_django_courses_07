from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy

class StudentListView(generic.ListView):
    model = Student
    
    def get_queryset(self):
        qs = super().get_queryset()
        if 'course_id' in self.request.GET:    
            course_id = self.request.GET['course_id']
            qs = qs.filter(courses=course_id)
        return qs

class StudentDetailView(generic.DetailView):
    model = Student

class StudentCreateView(generic.CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        mess_suc = 'Student %s %s has been successfully added.' % (form.cleaned_data['name'], form.cleaned_data['surname'])
        messages.success(self.request, mess_suc)
        return response
        
class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:edit')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
        
    def form_valid(self, form):
        response = super().form_valid(form)
        mess_suc = 'Info on the student has been successfully changed.'
        messages.success(self.request, mess_suc)
        return response

class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        mess_suc = 'Info on %s %s has been successfully deleted.' % (student.name, student.surname)
        messages.success(self.request, mess_suc)
        return response

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            mess_suc = 'Info on the student has been successfully changed.'
            messages.success(request, mess_suc)
            return redirect('/students/edit/'+pk)
    else:
        form = StudentModelForm(instance=student)           
    context = {'form': form}
    return render(request, 'students/edit.html', context)    
