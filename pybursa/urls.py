from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views
from feedbacks.views import FeedbackView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),
]
