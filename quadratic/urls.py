from django.conf.urls import url
from .views import quadratic_results

urlpatterns = [
    url(r'^$', quadratic_results, name="results"),
]
