
from django.conf.urls import url
from courses.views import detail

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
]
