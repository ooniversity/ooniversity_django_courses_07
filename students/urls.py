from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'add/$', views.StudentCreateView.as_view() , name='create'),
    url(r'edit/(?P<pk>[0-9]+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'remove/(?P<pk>[0-9]+)/$', views.StudentDeleteView.as_view() , name='remove'),
    url(r'^$', views.StudentListView.as_view(), name = 'list'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='detail'),
]