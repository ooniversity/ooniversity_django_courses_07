from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.student_list, name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.student_detail, name='detail'),
]
