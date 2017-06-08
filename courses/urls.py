from django.conf.urls import url
from courses.views import add_lesson,CourseDetailView,CourseCreateView,CourseUpdateView,CourseDeleteView

app_name='courses'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$',CourseDetailView.as_view(),name='detail'),
    url(r'^add/$',CourseCreateView.as_view(),name='add'),
    url(r'^edit/(?P<pk>\d+)/$',CourseUpdateView.as_view(),name='edit'),
    url(r'^remove/(?P<pk>\d+)/$',CourseDeleteView.as_view(),name='remove'),
    url(r'^(?P<course_id>\d+)/add_lesson/$',add_lesson,name='add-lesson'),
]