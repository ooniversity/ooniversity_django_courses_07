from django.conf.urls import url
from .views import detail

app_name='coaches'
urlpatterns = [
    url(r'^courses/(?P<coach_id>\d+)/$',detail,name='detail'),
]