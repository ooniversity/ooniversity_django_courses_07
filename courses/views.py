from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Course, Lesson
from django.contrib import messages
from .forms import CourseModelForm, LessonModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}

    return render(request, 'index.html', context)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'model_form'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course %s has been successfully added.' % (form.instance.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'
    context_object_name = 'model_form'
    pk_url_kwarg = 'course_id'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'course_id': self.kwargs.get('course_id')})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'course_id'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Deleted')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        model_form = LessonModelForm(request.POST)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (instance.subject))
            return redirect(reverse('courses:detail', kwargs={'course_id': course.id}))
    else:
        model_form = LessonModelForm(initial={'course': course_id})
    context = {'model_form': model_form}
    return render(request, 'courses/add_lesson.html', context)
