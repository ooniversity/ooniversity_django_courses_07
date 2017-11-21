
from django.conf.urls import url
from students.views import detail, list_view, create, edit, remove

app_name = 'students'
urlpatterns = [
    url(r'^$', list_view, name = 'list_view'),
    url(r'^(?P<st_id>[0-9]+)/$', detail, name = 'detail'),
    url(r'^add/$', create, name = 'add'),
    url(r'^(?P<pk>\d+)/remove/$', remove, name = 'remove'),
    url(r'^(?P<pk>\d+)/edit/$', edit, name = 'edit')
    
]
   
