
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render


urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
