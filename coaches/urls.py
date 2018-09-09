from django.conf.urls import url
from coaches import views


app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
]
