from django.shortcuts import redirect, render
from courses.models import Course, Lesson
from coaches.models import Coach
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST )
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            text = "Lesson {} has been successfully added.".format(data['subject'])
            messages.success(request, text)
            redirect_url = '/courses/{}/'.format(pk)
            return redirect(redirect_url)
    else:
        form = LessonModelForm(initial={"course":pk})
    return render(request, 'courses/add_lesson.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        text = "Course {} has been deleted.".format(course.name)
        messages.success(request, text)
        return redirect('/')
    return render(request, 'courses/remove.html', {'course': course})

def edit(request, pk):
    course = Course.objects.get(id = pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            text = "The changes have been saved."
            messages.success(request, text)
            # redirect_url = '/courses/{}/'.format(pk)
            return redirect('courses:edit',pk)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            text = "Course {} has been successfully added.".format(data['name'])
            messages.success(request, text)
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list']= Lesson.objects.all().filter(course = self.object)
        context['assistant_list']= Coach.objects.all().filter(assistant_courses = self.object)
        context['coach_list']= Coach.objects.all().filter(coach_courses = self.object)
        return context

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    form_class = CourseModelForm

    def form_valid(self, form):
        text = "Course {} has been successfully added.".format(form.cleaned_data['name'])
        messages.success(self.request, text)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Course creation"
        return context

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('courses:edit')
    form_class = CourseModelForm

    # def form_valid(self, form):
    #
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']="Course update"
        text = "The changes have been saved."
        messages.success(self.request, text)
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    #
    # def delete(self, request, *args, **kwargs):
    #     return super().delete( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        text = "Course {} has been deleted.".format(self.object.name)
        messages.success(self.request, text)
        context = super().get_context_data(**kwargs)
        context['title'] =  "Course deletion"
        return context