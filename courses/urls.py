from django.conf.urls import url

from . import views
from courses.models import Course
app_name = 'courses'
urlpatterns = [
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
] 
