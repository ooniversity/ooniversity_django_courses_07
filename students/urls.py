from django.conf.urls import url

from students import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/', views.create, name='add'),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name='remove'),
]

