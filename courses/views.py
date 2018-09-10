from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=context['course'])
        logger.debug("Courses detail view has been debugged!")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'form'
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course %s has been successfully added.' % form.cleaned_data['name'])
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'form'
    template_name = 'courses/edit.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context
    
    def get_success_url(self):
        return reverse('courses:edit', kwargs={'pk': self.object.id})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(request, 'Course %s has been deleted.' % self.object.name)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % new_lesson.subject)
            return redirect('courses:detail', course.id )
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})

