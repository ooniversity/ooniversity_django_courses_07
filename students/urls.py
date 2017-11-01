from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.slist, name='list'),
    url(r'^(?P<student_id>\d+)/$', views.sdetail, name='detail')
]