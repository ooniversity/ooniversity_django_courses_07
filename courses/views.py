from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Course,Lesson
from .forms import CourseModelForm,LessonModelForm

def by_course(request,course_id):
    course=Course.objects.get(pk=course_id)
    lessons=course.lesson_set.all()
    context={'course':course,'lessons':lessons}
    return render(request,'courses/by_course.html',context)
class CourseAddView(CreateView):
    template_name='courses/add.html'
    form_class=CourseModelForm
    success_url='/'

    def form_valid(self,form):
        messages.success(self.request,
                         "Студент {0} добавлен".format(form.instance.name))
        return super().form_valid(form)
    
class LessonAddView(CreateView):
    template_name='courses/add_lesson.html'
    form_class=LessonModelForm
    pk_url_kwarg = 'course_id'
    def get_initial(self):
        initial=super().get_initial()
        course_id=self.kwargs['course_id']
        initial['course']=Course.objects.get(pk=course_id)
        success_url=reverse_lazy('by_course',kwargs={'course_id':course_id})
        return initial
    def get_success_url(self):
        course_id=self.kwargs['course_id']
        success_url=reverse_lazy('by_course',kwargs={'course_id':course_id})
        return success_url
    def form_valid(self,form):
        messages.success(self.request,
                         "Урок {0} добавлен".format(form.instance.subject))
        return super().form_valid(form)
    
class CourseUpdateView(UpdateView):
    model=Course
    template_name='courses/edit.html'
    form_class=CourseModelForm
    context_object_name = 'course'
    success_url=None
    pk_url_kwarg = 'course_id'

    def form_valid(self,form):
        self.success_url=reverse_lazy('edit_course',kwargs={'course_id':form.instance.pk})
        messages.success(self.request,"Изменения сохранены")
        return super().form_valid(form)
    
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = '/'
    pk_url_kwarg = 'course_id'

    def delete(self,request,*args,**kwargs):
        course=Course.objects.get(pk=kwargs['course_id'])
        messages.success(request,"Курс {0} удален".format(course.name))
        return super().delete(self,request,*args,**kwargs)
    
