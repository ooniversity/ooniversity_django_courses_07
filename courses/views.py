from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
        context["course"] = self.object
        context["lessons"] = self.object.lesson_set.all()
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        fullname = form.instance.name
        messages.success(self.request, 'Course %s has been successfully added.' % fullname)
        return super().form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super().form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        response = super(CourseDeleteView, self).delete(self, request, *args, **kwargs)
        messages.success(request, 'Course %s has been deleted.' % self.object.name)
        return response


def index(request):
    courses = Course.objects.all()
    context = {"cour": courses}
    return render(request, 'index.html', context)


def add_lesson(request, id):
    course = Course.objects.get(id=id)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, ('Lesson %s has been successfully added.' % lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    context = {'form': form, 'course': course}
    return render(request, 'courses/add_lesson.html', context)