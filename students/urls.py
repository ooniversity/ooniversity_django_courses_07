from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    # url(r'^$', views.list_view, name='students'),
    url(r'^$', views.StudentListView.as_view(), name = 'list_view'),
    # url(r'^(course_id=?P<pk>[0-9]+)/$', views.StudentListView.as_view(), name = 'list_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentsDetailView.as_view(), name='detail'),
]