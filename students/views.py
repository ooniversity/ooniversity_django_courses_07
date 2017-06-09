from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students


# class StudentListView(ListView):
#     model = Student
#     # template_name = 'students/student_list.html'

#     def get_queryset(self):
#         course_id = self.request.GET.get('course_id', None)
#         if course_id:
#             students = Student.objects.filter(courses=course_id)
#         else:
#             students = Student.objects.all()
#         paginator = Paginator(students, 2)
#         page = self.request.GET.get('page')
#         try:
#             students = paginator.page(page)
#         except PageNotAnInteger:
#             students = paginator.page(1)
#         except EmptyPage:
#             students = paginator.page(paginator.num_pages)
#         return students


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        fullname = form.instance.name + ' ' + form.instance.surname
        messages.success(self.request, 'Student %s has been successfully added.' % fullname)
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get('pk'))
        messages.success(self.request, 'Info on %s has been successfully deleted.' % student)
        return super().delete(self, request, *args, **kwargs)