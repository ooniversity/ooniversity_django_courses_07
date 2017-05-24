from django.conf.urls import url
from students import views

#app_name = 'students'
urlpatterns = (
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
)