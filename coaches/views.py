from django.shortcuts import render
from coaches.models import Coach


def detail(request, param):
	one_coach = Coach.objects.get(id__exact = int(param))
	context = {"coach": one_coach}
	return render(request, 'coaches/detail.html', context)
