
from django.shortcuts import render
from students.models import Student


def list_view(request):
	if request.GET:
		n = request.GET[u'course_id']
		stud = Student.objects.filter(courses=int(n))
		context = {'stud': stud}
		return render(request, 'students/list.html', context)
	stud = Student.objects.all()
	context = {"stud": stud}
	return render(request, 'students/list.html', context)


def detail(request, pk):
	stud = Student.objects.get(id__exact = int(pk))
	context = { "stud": stud }
	return render(request, 'students/detail.html', context)
