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
from quadratic.views import quadratic_results
from courses.views import index
from feedbacks.views import FeedbackView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^quadratic/results/$', quadratic_results, name='quadratic_results'), #(?P<a>\d+)/(?P<b>\d+)/(?P<c>\d+)/
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
