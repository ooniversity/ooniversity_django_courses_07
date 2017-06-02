from django.conf.urls import url, include
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<id>[0-9]+)/add_lesson$', views.add_lesson, name='add_lesson'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<id>[0-9]+)/$', views.remove, name='remove'),
]