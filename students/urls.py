from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [    
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view')
    ]
    
