from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import logging


logger = logging.getLogger(__name__)



class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        logger.debug("Students detail view has been debugged!")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context
    

class StudentListView(ListView):
    model = Student
    paginate_by = 2
        
    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs    
    

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy ('students:list_view')
    form_class = StudentModelForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
	
    def form_valid(self, form):
        fullname = form.instance.name + ' ' + form.instance.surname
        messages.success(self.request, 'Student %s has been successfully added.' % fullname)
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy ('students:list_view')
    form_class = StudentModelForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
	
    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed')
        return super().form_valid(form)

    
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy ('students:list_view')   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
	
    def delete(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get('pk'))
        messages.success(self.request, 'Info on %s has been successfully deleted.' % student)
        return super().delete(self, request, *args, **kwargs)



