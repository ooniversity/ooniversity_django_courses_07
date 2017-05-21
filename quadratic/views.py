from django.shortcuts import render


def quadratic_results(request):
    print('========================================')
    return render(request, 'results.html')
