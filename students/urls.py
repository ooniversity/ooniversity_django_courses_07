from django.conf.urls import include, url
from students.views import list_view, detail


app_name = 'students'
urlpatterns = [
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<id>[0-9]+)/$', detail, name='detail'),
]