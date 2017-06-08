from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Student
from .forms import StudentModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def edit(request, student_id):
    instance = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        model_form = StudentModelForm(request.POST, instance=instance)
        if model_form.is_valid():
            instance = model_form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect(reverse('students:edit', kwargs={'student_id': instance.id}))
    else:
        model_form = StudentModelForm(instance=instance)
    context = {'model_form': model_form}
    return render(request, 'students/edit.html', context)


def remove(request, student_id):
    instance = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Info on %s has been successfully deleted.' % (instance.fullname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html')


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id != None and course_id.isnumeric():
            qs = Student.objects.filter(courses__id__exact=course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student %s has been successfully added.' % (form.instance.fullname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self):
        return reverse_lazy('students:edit', kwargs={'pk': self.kwargs.get('pk')})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Deleted')
        return response