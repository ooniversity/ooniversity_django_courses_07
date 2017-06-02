from django.conf.urls import include, url
from courses.views import index, detail

app_name = 'courses'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', detail, name='detail'),
]
