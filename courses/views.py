from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.urls import reverse_lazy
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView

def index(request):
    courses = Course.objects.all()
    return render(request,'index.html',{'Courses':courses})

#подробности курса
class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lesson_set.all()
        context['title'] = 'Course detail'
        return context


#Добавлении курса
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        fullname = form.instance.name
        messages.success(self.request, 'Course %s has been successfully added.' % fullname)
        return super().form_valid(form)

#Изменении курса
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def get_success_url(self):
        url = reverse_lazy('courses:edit',kwargs={'pk':self.kwargs['pk']})
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super().form_valid(form)


#Удаления курса
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

#Добавления урока
def add_lesson(request,course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, ('Lesson %s has been successfully added.' % lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        form = LessonModelForm(initial={'course':course_id})
    return render(request,'courses/add_lesson.html',{'form':form})