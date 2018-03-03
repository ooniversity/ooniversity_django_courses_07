from students.models import Student
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

import logging
logger = logging.getLogger(__name__)


class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
        qs = super().get_queryset()
        if 'course_id' in self.request.GET:    
            course_id = self.request.GET['course_id']
            qs = qs.filter(courses=course_id)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'course_id' in self.request.GET:    
            course_id = self.request.GET['course_id']
            context['course_id'] = course_id
        return context

class StudentDetailView(generic.DetailView):
    logger.debug('Students detail view has been debugged!')
    logger.info('Logger of students detail view informs you!')
    logger.warning('Logger of students detail view warns you!')
    logger.error('Students detail view went wrong!')

    model = Student

class StudentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')
    success_message = 'Student %(name)s %(surname)s has been successfully added.'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
         
class StudentUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Student
    fields = '__all__'
    success_message = 'Info on the student has been successfully changed.'
    
    def get_success_url(self):
        return reverse('students:edit', args=[self.object.id])
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    success_message = 'Info on %s %s has been successfully deleted.'

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, self.success_message % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
