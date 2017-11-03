from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<student_id>\d+)/$', views.StudentDetailView.as_view(pk_url_kwarg = 'student_id'), name='detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<student_id>\d+)/$', views.StudentUpdateView.as_view(pk_url_kwarg = 'student_id'), name='update'),
    url(r'^remove/(?P<student_id>\d+)/$', views.StudentDeleteView.as_view(pk_url_kwarg='student_id'), name='delete')
]