from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import Course,Lesson
from .forms import CourseModelForm

def by_course(request,course_id):
    course=Course.objects.get(pk=course_id)
    lessons=course.lesson_set.all()
    context={'course':course,'lessons':lessons}
    return render(request,'courses/by_course.html',context)
class CourseAddView(CreateView):
    template_name='courses/add.html'
    form_class=CourseModelForm
    success_url='/'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['message']="Курс {0} добавлен!".format(self.object)
        print(self.object)
        return context
    def form_valid(self,form):
        messages.success(self.request,
                         "Запись {0} добавлена".format(form.instance.name))
        return super().form_valid(form)
        

    

