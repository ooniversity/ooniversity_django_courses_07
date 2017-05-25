from django.conf.urls import url
from students.views import list_view, detail

app_name = 'students'
urlpatterns = (
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
)