from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentDetailView(DetailView):
    model = Student
#def detail(request, pk):
    #student = get_object_or_404(Student, pk=pk)
    #context = {'student': student }
    #return render (request, 'students/detail.html', context)

class StudentListView(ListView):
    model = Student    
    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id :
            qs = Student.objects.filter(courses__id=course_id)
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
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"Student {} {} has been successfully added.".format(self.object.name, self.object.surname))
        return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Student registration", 'header':"Добавить студента",
                        'button':"Создать"})
        return context
                         
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
    form_class = StudentModelForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,  "Info on the student has been successfully changed.")
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Student info update", 'header':"Редактирование данных студента",
                        'button':"Изменить"})
        return context

    def get_success_url(self):
        success_url = reverse_lazy('students:edit',
                                   kwargs={"pk":self.object.id})
        return success_url
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
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    def delete(self, request, *args, **kwargs):
        response = super().delete( request, *args, **kwargs)
        messages.success(self.request,
                         "Info on {} {} has been successfully deleted.".format(self.object.name, self.object.surname))
        return response
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
