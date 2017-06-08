from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [    
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    ]
    
