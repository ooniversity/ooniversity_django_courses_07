from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
]
