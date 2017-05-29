from django.conf.urls import url,include
from . import views
app_name = 'students'
urlpatterns = [
    url(r'^(?P<student_id>[0-9]+)/$',views.student_detail,name='detail'),
]