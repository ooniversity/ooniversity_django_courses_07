from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


import logging
logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        qs = super().get_queryset()
        logger.debug("Courses detail view has been debugged!")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return qs


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'short_description', 'description', 'coach', 'assistant']
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Course %s has been successfully added." % (form.instance.name))
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'short_description', 'description', 'coach', 'assistant']
    template_name = 'courses/edit.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course update"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Course %s has been deleted." % self.object.name)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context


def index(request):

    courses_list = Course.objects.all()
    return render(request, "index.html", {"courses_list": courses_list})


def add_lesson(request, pk):

    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.course = Course.objects.get(id=pk)
            instance.save()
            messages.success(request, "Lesson %s has been successfully added." % instance.subject)
            return redirect('courses:detail', pk = pk)
    else:
         form = LessonModelForm(initial={'course': pk, })

    return render(request, "courses/add_lesson.html", {'form': form })

