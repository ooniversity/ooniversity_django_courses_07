from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.views import Coach
    
def detailview(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'courses/detail.html', {'course': course})
