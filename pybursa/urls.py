"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name = 'index'),
    url(r'^contact/$', views.contact, name = 'contact'),
    # url(r'^student_list/$', views.student_list, name = 'student_list'),
    # url(r'^student_detail/$', views.student_detail, name = 'student_detail'),

    url(r'^quadratic/', include('quadratic.urls')),

    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
]
