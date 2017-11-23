
from django.conf.urls import include, url
from courses.views import add_lesson
from courses import views
app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view(), name = 'detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name = 'add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.CourseUpdateView.as_view(), name = 'edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(), name = 'remove'),
    url(r'^(?P<pk>[0-9]+)/add_lesson/$', add_lesson, name = 'add-lesson')
]
   
