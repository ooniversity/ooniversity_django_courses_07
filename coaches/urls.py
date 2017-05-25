from django.conf.urls import include, url
from .views import detail


app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', detail, name='detail'),
]