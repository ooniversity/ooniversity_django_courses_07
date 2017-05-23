from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^results/(?P<a>.*)$', views.results, name='results'),
]

#(?P<a>.*)(&P<b>.*)(&P<c>.*)