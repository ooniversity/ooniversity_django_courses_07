from django.conf.urls import url

from courses import views

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/', views.create, name='add'),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),

]

