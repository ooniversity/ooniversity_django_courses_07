from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.detailview, name='detail'),
]
