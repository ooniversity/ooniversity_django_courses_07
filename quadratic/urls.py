from django.conf.urls import url

from quadratic import views

urlpatterns = [
    url(r'results/$', views.quadratic_results, name='results'),
]

