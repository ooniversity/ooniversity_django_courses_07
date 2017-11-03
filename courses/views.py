from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course
from .forms import CourseModelForm, LessonModelForm

# Create your views here.
class CourseDetailView(DetailView):
    
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course_id'] = self.object.id
        
        return context
    
    
class CourseCreateView(CreateView):
    
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
      
        return context
        
        
    def form_valid(self, form):
        messages.success(self.request, 'Course {} has been successfully added.'.format(form.cleaned_data['name']))
        
        return super().form_valid(form)
    
    
class CourseUpdateView(UpdateView):
    
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
      
        return context
        
        
    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('courses:edit', args=[self.object.id])


class CourseDeleteView(DeleteView):
    
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        
        return context
    
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        
        return super().delete(request, *args, **kwargs)



def add_lesson(request, course_id):
    form = LessonModelForm(initial={'course': course_id})
    
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson {} has been successfully added.'.format(form.cleaned_data['subject']))
            
            return redirect('courses:detail', course_id=course_id)  
    
    return render(request, 'courses/add_lesson.html', {'form': form})