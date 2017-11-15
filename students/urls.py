
from django.conf.urls import include, url
from students.views import list_view, detail


urlpatterns = [
    url(r'^$', list_view, name = 'list_view'),
    url(r'^(?P<st_id>[0-9]+)/$', detail, name = 'detail_student')
]
   
