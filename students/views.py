from django.shortcuts import render
from .models import Student, Course
from django.views import generic
# Create your views here.
def list_view(request):
    if request.method == 'GET':
        course_id = request.GET.get('course_id')
        students = Student.objects.all().filter(courses = Course.objects.filter(id = course_id) )
    else:
        students = Student.objects.all()
    context = {'student_list': students, }
    return render(request, 'students/list.html', context)

class StudentsDetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'


class StudentListView(generic.ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            return qs.filter(courses__id=course_id)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context