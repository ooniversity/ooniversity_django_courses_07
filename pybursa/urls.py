from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^admin/', admin.site.urls),	
	url(r'^polls/', include('polls.urls')),
	url(r'^quadratic/', include('quadratic.urls')),
	url(r'^courses/', include('courses.urls')),
	url(r'^students/', include('students.urls')),
	url(r'^coaches/', include('coaches.urls')),
]
admin.site.site_header = 'PyBursa Administration'
