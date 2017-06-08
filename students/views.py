from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from students.models import Student
from .forms import StudentModelForm


#список всех студентвои и одного курса
class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

#данные студента одного
class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'


#создание студента
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        fullname = form.instance.name + ' ' + form.instance.surname
        messages.success(self.request, 'Student %s has been successfully added.' % fullname)
        return super().form_valid(form)


#Редактирования студента
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super().form_valid(form)

#Удаления
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/remove.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(self, request, *args, **kwargs)
        student = self.object.name + ' ' + self.object.surname
        messages.success(request, "Info on %s has been successfully deleted." % student)
        return response