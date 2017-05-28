from django.conf.urls import url
from . import views

app_name='coaches'
urlpatterns = [
    url(r'^courses/(?P<coach_id>\d+)/$',views.detail,name='detail'),
]