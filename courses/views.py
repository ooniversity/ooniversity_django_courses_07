from django.shortcuts import render, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


class CourseCreateView(SuccessMessageMixin, generic.CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('index')
    success_message = 'Course %(name)s has been successfully added.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

class CourseUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'
    context_object_name = 'form'
    success_message = 'The changes have been saved.'

    def get_success_url(self):
        return reverse('courses:edit', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

class CourseDeleteView(generic.DeleteView):
    model = Course
    fields = '__all__'
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    success_message = 'Course %s has been deleted.'

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['pk'])
        messages.success(self.request, self.success_message % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            mess_suc = 'Lesson %s has been successfully added.' % form.cleaned_data['subject']
            messages.success(request, mess_suc)
            return redirect('/courses/'+pk)
    else:
        form = LessonModelForm(initial={'course': pk})           
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)
