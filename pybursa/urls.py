from django.conf.urls import include, url
from django.contrib import admin
from . import views
from quadratic.views import quadratic_results

urlpatterns = [
    url(r'^', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^quadratic/results/$', quadratic_results, name='quadratic_results'), 
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
admin.site.site_header = 'PyBursa Administration'
