from django.shortcuts import render
from django.contrib import messages
from courses.models import Course
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentModelForm
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.views.generic.edit import DeleteView

class StudentListView(ListView):
    model=Student
    template_name='students/students.html'
    context_object_name = 'students'
    def get_queryset(self):
        c_pk=self.request.GET.get('course_id',False)
        if not c_pk:
            return super().get_queryset()
        else:
            course=Course.objects.get(pk=c_pk)
            students=course.student_set.all()
            return students
class StudentDetailView(DetailView):
    pk_url_kwarg = 'student_id'
    context_object_name='student'
    model=Student
class StudentCreateView(CreateView):
    model=Student
    form_class=StudentModelForm
    success_url='/'
    template_name='add.html'

    def form_valid(self,form):
        messages.success(self.request,
                         "Запись {0} добавлена".format(form.instance.name))
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Добавление нового студента'
        return context
class StudentUpdateView(UpdateView):
    model=Student
    template_name='edit.html'
    form_class=StudentModelForm
    context_object_name = 'student'
    success_url=None
    pk_url_kwarg = 'student_id'

    def form_valid(self,form):
        self.success_url=reverse_lazy('edit_student',kwargs={'student_id':form.instance.pk})
        messages.success(self.request,"Изменения сохранены")
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Изменение студента'
        return context
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'remove.html'
    context_object_name = 'student'
    success_url = '/'
    pk_url_kwarg = 'student_id'

    def delete(self,request,*args,**kwargs):
        course=self.get_object()
        messages.success(request,"Курс {0} удален".format(course.name))
        return super().delete(self,request,*args,**kwargs)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Удаление студента'
        return context
