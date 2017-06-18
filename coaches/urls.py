from django.conf.urls import url
from coaches.views import detail

app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<coach_id>[0-9]+)/$', detail, name='detail'),
]