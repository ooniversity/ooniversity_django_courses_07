
from django.conf.urls import include, url
from courses.views import detail, add, remove, edit, add_lesson

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<cd_id>[0-9]+)/$', detail, name = 'detail'),
    url(r'^add/$', add, name = 'add'),
    url(r'^edit/(?P<pk>[0-9]+)$', edit, name = 'edit'),
    url(r'^remove/(?P<pk>[0-9]+)$', remove, name = 'remove'),
    url(r'^(?P<pk>[0-9]+)/add_lesson/$', add_lesson, name = 'add-lesson')
]
   
