from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove, name='remove'),
    url(r'^(?P<pk>[0-9]+)/add_lesson/$', views.add_lesson, name='add_lesson'),
]
