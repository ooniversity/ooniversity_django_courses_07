from django.shortcuts import render
from courses.models import Course, Lesson


def index(request):
	cour = Course.objects.all()
	context = {"cour": cour}
	return render(request, 'index.html', context)


def detail(request, pk):
	one_c = Course.objects.get(id__exact = int(pk))
	lessons = Lesson.objects.filter(course__id__exact = int(pk))
	context = {"course": one_c, "lessons": lessons}
	return render(request, 'courses/detail.html', context)
