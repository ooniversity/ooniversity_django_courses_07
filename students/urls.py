from django.conf.urls import url
from students import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='list'),
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^remove/(\d+)/$', views.remove, name='remove'),
]
