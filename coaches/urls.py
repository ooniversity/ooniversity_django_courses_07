from django.conf.urls import url
from coaches.views import detail

app_name = 'coaches'
urlpatterns = (
    url(r'^(?P<param>\d+)/$', detail, name='detail'),
)
