from django.conf.urls import include, url
from courses.views import index, detail, add, edit, remove, add_lesson

app_name = 'courses'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^courses/(?P<course_id>\d+)/$', detail, name='detail'),
    url(r'^courses/add/$', add, name='add'),
    url(r'^courses/edit/(?P<pk>\d+)/$', edit, name='edit'),
    url(r'^courses/remove/(?P<pk>\d+)/$', remove, name='remove'),
    url(r'^courses/(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add_lesson'),
]
