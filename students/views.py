#from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from students.models import Student
from students.forms import StudentModelForm

import logging
logger = logging.getLogger('pybursa.students')

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged!")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context
    

#def detail(request, pk):
    #student = get_object_or_404(Student, pk=pk)
    #context = {'student': student }
    #return render (request, 'students/detail.html', context)

class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
 #       context['page_title'] = self.page_title
        context['page_path'] = ''
        return context
    
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id :
            qs = qs.filter(courses__id=course_id)
        return qs
        
#def list_view(request):
    #course_id = request.GET.get('course_id', None)
    #if course_id :
       # students = Student.objects.filter(courses__id=course_id)        
    #else:
       #students = Student.objects.all()
   # context = {'students': students}
   # return render (request, 'students/list.html', context)

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    #form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')


    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
    
    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been successfully added.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)
        
    
                         
#def create(request):
 #   if request.method == "POST":
  #      form = StudentModelForm(request.POST)
   #     if form.is_valid():
    #        instance = form.save()           
     #       messages.success(request,  "Student {} has been successfully added.".format(instance.name)
      #      return redirect ('students:list_view')       
    #else:
     #   form = StudentModelForm()   
    #context = {'form': form}
    #return render (request, 'students/add.html', context)

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'  # to avoid ImproperlyConfigured error
    #form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    #def get_success_url(self):
    #    success_url = reverse_lazy('students:edit',
    #                               kwargs={"pk":self.object.id})
    #    return success_url
#def edit(request, pk):
 #   student = Student.objects.get(id=pk)
  #  if request.method == "POST":
   #     form = StudentModelForm(request.POST, instance=student)
    #    if form.is_valid():
     #       student = form.save()
      #      messages.success(request, "Info on the student has been successfully changed.")
       #     return redirect ('students:edit', student.id)       
  #  else:
   #     form = StudentModelForm(instance=student)   
    #context = {'form': form}
    #return render (request, 'students/edit.html', context)

class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'  # to avoid ImproperlyConfigured error
    #form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Info on %s %s has been successfully deleted.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

                         
#def remove(request, pk):
 #   student = Student.objects.get(id=pk)
  #  if request.method == "POST":
   #     student.delete()
    #    messages.success(request, "Info on %s has been successfully deleted."%student.name)
     #   return redirect ('students:list_view')
#    print(redirect ('index'))
 #   context = {'student': student}
  #  return render (request, 'students/remove.html', context)


# Create your views here.
