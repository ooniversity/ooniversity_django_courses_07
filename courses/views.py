from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

# Create your views here.

def index(request):
    courses_list = Course.objects.all()
    context = {'courses_list':courses_list}
    return render(request, 'index.html', context)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Информация о курсе'
        context['lessons'] = Lesson.objects.filter(course_id = self.object.id)
        return context

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'item'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Course has been successfully added.")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Course creation'
        return context
        
class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'item'
     
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Course update'
        return context
        
    def get_success_url(self):
        return reverse_lazy('courses:edit', args=[self.object.id])
    
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'item'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Course deletion'
        return context  
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Info on course has been successfully deleted.")
        return response    
        

def add_lesson(request, pk):
    form = LessonModelForm(initial={'course' : Course.objects.get(id=pk)})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, "Lesson " + new_lesson.subject + " has been successfully added.")
            return redirect('courses:detail', cd_id=pk)
    return render(request, 'courses/add_lesson.html', {'form': form})
