from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson')
]