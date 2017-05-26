from django.conf.urls import url, include
from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
]