from django.shortcuts import render
from django.http import HttpResponse
from math import sqrt
from quadratic.forms import QuadraticForm


def quadratic_results(request):

    if request.GET == {}:
        form = QuadraticForm()
        context = {'form': form}
    else:
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            quadratic = QuadraticEquation(**form.cleaned_data)
            quadratic.get_results()
            context['results'] = quadratic
    return render(request, 'quadratic/results.html', context)


class QuadraticEquation:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = self.b * self.b - 4 * self.a * self.c

    def get_results(self):
        if self.d > 0:
            self.x1 = (-1 * self.b + sqrt(self.d)) / (2 * self.a)
            self.x2 = (-1 * self.b - sqrt(self.d)) / (2 * self.a)
        elif self.d == 0:
            self.x1 = (-1 * self.b + sqrt(self.d)) / (2 * self.a)

            
