from django.conf.urls import include, url
from django.contrib import admin
from quadratic.views import quadratic_results
from courses.views import IndexView, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^quadratic/results/', quadratic_results, name='results'),
    url(r'^contact/', contact, name='contact'),

    url(r'^polls/', include('polls.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls'))]

admin.site.site_header = 'PyBursa Administration'
