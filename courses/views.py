# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .forms import LessonModelForm, CourseModelForm
from .models import Course


class CourseDetailView(DetailView):
    model = Course
    fields = '__all__'
    template_name = 'courses/detail.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'  # to avoid ImproperlyConfigured error
    # form_class = CourseModelForm
    # form = CourseModelForm
    template_name = 'courses/add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Course %s has been successfully added.' % (data['name']))
        return super(CourseCreateView, self).form_valid(form)

    # def form_valid(self, form):
    #     super_valid = super(CourseCreateView, self).form_valid(form)
    #     messages.success(self.request,
    #                      'Course {} has been successfully added.'.format(self.object.name))
    #     return super_valid


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'  # to avoid ImproperlyConfigured error
    template_name = 'courses/edit.html'
    context_object_name = 'form'
    # success_url = reverse_lazy('index')
    # success_url = '/courses/edit/%(id)d/'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        data = form.instance
        messages.success(self.request, 'The changes have been saved.')
        self.success_url = reverse_lazy('courses:edit', args=(data.id,))
        return super(CourseUpdateView, self).form_valid(form)

    # def form_valid(self, form):
    #     messages.success(self.request, 'The changes have been saved.')
    #     return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    fields = '__all__'  # to avoid ImproperlyConfigured error
    template_name = 'courses/remove.html'
    context_object_name = 'form'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, 'Course %s has been deleted.' % (course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     delete_super = super(CourseDeleteView, self).delete(request, *args, **kwargs)
    #     messages.success(self.request,
    #                      'Course {} has been deleted.'.format(self.object.name))
    #     return delete_super


def add_lesson(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {} has been successfully added.'.format(lesson.subject))
            return redirect('courses:detail', lesson.course_id)
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})
