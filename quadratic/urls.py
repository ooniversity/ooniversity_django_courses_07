from django.conf.urls import url
from .views import quadratic_results

urlpatterns = [
    url(r'^results/$', quadratic_results, name="results"),
]
