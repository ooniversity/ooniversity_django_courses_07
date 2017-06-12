from django.shortcuts import render, redirect, get_object_or_404, reverse
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course_inf'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['course_plan'] = self.object.lesson_set.all()
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    form_class = CourseModelForm
    template_name = 'courses/add.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course {} has been successfully added.'.format(form.instance.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context



class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context



def add_lesson(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (instance.subject))
            return redirect(reverse('courses:detail', kwargs={'course_id': course.id}))
    else:
        form = LessonModelForm(initial={'course': course.id})
    return render(request, 'courses/add_lesson.html', {'form': form})