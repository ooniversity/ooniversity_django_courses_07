from django.conf.urls import url
from students.views import list_view, detail, create, edit, remove

app_name = 'students'
urlpatterns = (
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^add/$', create, name='create'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', remove, name='remove'),
)