from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses/([0-9]+)/$', views.detail, name='detail')
]
