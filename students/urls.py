from django.conf.urls import include, url
from students.views import list_view, detail, add, edit, remove


app_name = 'students'
urlpatterns = [
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', remove, name='remove'),
]