from django.conf.urls import url
from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^add/$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
]