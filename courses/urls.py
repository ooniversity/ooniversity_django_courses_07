from django.conf.urls import url
from courses import views

app_name = 'courses'
urlpatterns = [
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^(\d+)/add_lesson/$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^remove/(\d+)/$', views.remove, name='remove'),
]
