from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.student_list, name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.student_detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove, name='remove'),]
