from django.shortcuts import render

def results(request, a):
    return render(request, "quadratic/results.html", {'a': a})

