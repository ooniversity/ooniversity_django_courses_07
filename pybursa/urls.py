from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import index, contact
from quadratic.views import quadratic_results


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^polls/', include('polls.urls')),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^quadratic/results/$', quadratic_results, name='results')
]