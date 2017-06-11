from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def index(request):
    context = {'courses_list': Course.objects.all()}
    return render(request, 'index.html', context)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Course %s has been successfully added.' % form.instance)
        return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    form_class = CourseModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    form_class = CourseModelForm
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(request, ("Course %s has been deleted." % self.object.name))
        return response


def add_lesson(request, course_id):
    get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson.subject)
            return redirect(reverse('courses:detail', kwargs={'course_id': course_id}))
    else:
        form = LessonModelForm(initial={'course': course_id})

    return render(request, 'courses/add_lesson.html', {'form': form})
