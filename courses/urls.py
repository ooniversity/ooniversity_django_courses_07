from django.conf.urls import include, url
from courses.views import list_view, detail

app_name = 'courses'
urlpatterns = [
    url(r'^$', list_view, name='list_view'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', detail, name='detail'),
]
