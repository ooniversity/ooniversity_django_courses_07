from django.conf.urls import include, url
from courses.views import detail, add, edit, remove, add_lesson


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', remove, name='remove'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add-lesson')
]