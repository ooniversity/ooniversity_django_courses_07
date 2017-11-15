
from django.conf.urls import url
from students.views import detail, list_view

app_name = 'students'
urlpatterns = [
    url(r'^$', list_view, name = 'list_view'),
    url(r'^(?P<st_id>[0-9]+)/$', detail, name = 'detail')
]
   
