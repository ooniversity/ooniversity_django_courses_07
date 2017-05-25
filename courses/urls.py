from django.conf.urls import url
from courses.views import index, courses

app_name = 'courses'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^courses/(?P<course_id>[0-9]+)/$', courses, name='courses'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
