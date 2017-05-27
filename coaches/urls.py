from django.conf.urls import url

from . import views

app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<coaches_id>[0-9]+)/$', views.detail, name='detail'),
]
