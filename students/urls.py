from django.conf.urls import url
from . import views

app_name='students'
urlpatterns = [
    url(r'^students/$',views.list_view,name='list_view'),
    url(r'^students/(?P<student_id>\d+)$',views.detail,name='detail'),
]