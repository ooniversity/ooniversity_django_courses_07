from django.shortcuts import redirect, render
from courses.models import Course, Lesson
from coaches.models import Coach
from django.views import generic
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages

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
            redirect_url = '/courses/{}/'.format(pk)
            return redirect(redirect_url)
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

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

    # def get_queryset(self):
    #     self.object = get_object_or_404(Course, name=self.object[0])
    #     return Course.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list']= Lesson.objects.all().filter(course = self.object)
        context['assistant_list']= Coach.objects.all().filter(assistant_courses = self.object)
        context['coach_list']= Coach.objects.all().filter(coach_courses = self.object)
        return context
