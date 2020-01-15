from django.shortcuts import render


def quadratic_results(request):
    print(request.method)
    return render(request, 'results.html', {'get': request.GET})
