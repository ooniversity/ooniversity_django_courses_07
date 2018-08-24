from django.conf.urls import url
from . import views

app_name = 'coaches'
urlpatterns = [
    url(r'^(\d+)/$', views.detail, name='detail'),
]
