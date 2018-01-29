from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/edit.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        text = "Info on the student has been successfully changed."
        messages.success(self.request, text)
        return context


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/remove.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  "Student suppression"
        text = "Info on {} {} has been successfully deleted.".format(self.object.name, self.object.surname)
        messages.success(self.request, text)
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        text = "Student {} {} has been successfully added.".format(form.cleaned_data['name'], form.cleaned_data['surname'])
        messages.add_message(self.request, messages.SUCCESS, text)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] =  "Student registration"
        return context


#
def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            text = "Student {} {} has been successfully added.".format(data['name'], data['surname'])
            messages.success(request, text)
            return redirect('/students/')
    else:
        form = StudentModelForm()
        return render(request, 'students/add.html', {'form': form})


# def list_view(request):
#     if request.method == 'GET':
#         course_id = request.GET.get('course_id')
#         students = Student.objects.all().filter(courses=Course.objects.filter(id=course_id))
#     else:
#         students = Student.objects.all()
#     context = {'student_list': students, }
#     return render(request, 'students/list.html', context)


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'


class  StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            return qs.filter(courses__id=course_id)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
