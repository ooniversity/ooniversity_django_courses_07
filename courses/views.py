from django.shortcuts import render
from courses.models import Course, Lesson
from django.views import generic
from coaches.views import Coach

def contact(request):
    return render(request, 'courses/contact.html')

class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'qs_list'
    
    def get_queryset(self):
        return Course.objects.all()
    
def detailview(request, pk):
    qscurrent = Course.objects.get(id=pk)
    qsdetail_list = Lesson.objects.filter(course = pk)
    coach = Coach.objects.get(id=qscurrent.coach.id)
    assistant = Coach.objects.get(id=qscurrent.assistant.id)
    return render(request, 'courses/detail.html',     context = {
                                                                 'pk': pk,
                                                                 'qsdetail_list': qsdetail_list,
                                                                 'qscurrent': qscurrent,
                                                                 'coach': coach,
                                                                 'assistant': assistant })    
