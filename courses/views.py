from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lesson_set.all().order_by('order')
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/form.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        messages.success(self.request, 
            'Course %s has been successfully added.' % form.instance.name)
        return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/form.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course updated'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super().form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs.get('pk'))
        messages.success(self.request, 'Course %s has been deleted.' % course)
        return super().delete(self, request, *args, **kwargs)


def add_lesson(request, course_pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 
                'Lesson %s has been successfully added.' % instance.subject)
            return redirect('courses:detail', course_pk)
    else:
        form = LessonModelForm(initial={'course':course_pk})
        print(form)
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)