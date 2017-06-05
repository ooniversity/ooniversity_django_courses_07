from django.conf.urls import url
from quadratic.views import quadratic_results


app_name = 'quadratic'
urlpatterns = [
    url(r'^results/$', quadratic_results, name='results'),
]
