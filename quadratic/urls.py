from django.conf.urls import url
from quadratic import views


app_name = 'quadratic'
urlpatterns = [
    url(r'^results/$', views.quadratic_results, name='results'),
]
