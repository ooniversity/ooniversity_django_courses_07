from django.shortcuts import render
from quadratic.quadratic import QuadraticEquation
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.GET == {}:
        form = QuadraticForm()
        context = {'form': form}
    else:
        form = QuadraticForm(request.GET)
        context = {'form': form}
        if form.is_valid():
            result = QuadraticEquation(**form.cleaned_data)
            result.solve()
            context['result'] = result
    return render(request, 'quadratic/results.html', context)
