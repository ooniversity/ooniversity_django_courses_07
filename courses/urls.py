from django.conf.urls import url

from . import views


urlpatterns = [    
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    ]
    
