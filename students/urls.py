from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'add/$', views.StudentsCreateView.as_view() , name='create'),
    url(r'edit/(?P<pk>[0-9]+)/$', views.StudentsUpdateView.as_view(), name='edit'),
    url(r'remove/(?P<pk>[0-9]+)/$', views.StudentsDeleteView.as_view() , name='remove'),
    url(r'^$', views.StudentListView.as_view(), name = 'list_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentsDetailView.as_view(), name='detail'),
]