from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    
    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


def list_view(request): 

    course_id = request.GET.get('course_id', '')
    
    if course_id == '':
        student_list = Student.objects.all()
    else:
        student_list = Student.objects.filter(courses=course_id)

    return render(request, "students/list.html", {"student_list": student_list })


def detail(request, student_id): 

    student_obj = Student.objects.get(id=student_id)
    courses_list = student_obj.courses.all()

    return render(request, "students/detail.html", {"student": student_obj, "courses_list": courses_list })


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student %s %s has been successfully added." % (form.instance.name, form.instance.surname))
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context


def create(request):

    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Student %s %s has been successfully added." % (instance.name, instance.surname))
            return redirect('students:list_view')

    else:
         form = StudentModelForm()

    return render(request, "students/add.html", {'form': form })


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


def edit(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('students:edit', student_id = student.id)
    else:
        form = StudentModelForm(instance=student)

    return render(request, "students/edit.html", {'form': form })


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Info has been successfully deleted.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context


def remove(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s %s has been successfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')

    return render(request, "students/remove.html", {'student': student })



