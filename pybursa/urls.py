from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import contact
from courses.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact/', contact, name='contact'),
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^admin/', admin.site.urls),
]
