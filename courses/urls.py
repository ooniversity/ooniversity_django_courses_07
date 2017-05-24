from django.conf.urls import include, url
from courses.views import detail


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', detail, name='detail')
]