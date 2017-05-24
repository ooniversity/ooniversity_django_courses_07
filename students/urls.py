from django.conf.urls import url
from students.views import detail

app_name = 'students'
urlpatterns = (
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
)