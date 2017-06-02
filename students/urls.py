from django.conf.urls import url
from students.views import list_view,detail,create,edit, remove

app_name='students'
urlpatterns = [
    url(r'^$',list_view,name='list_view'),
    url(r'^(?P<student_id>\d+)/$',detail,name='detail'),
    url(r'^add/$',create,name='add'),
    url(r'^edit/(?P<student_id>\d+)/$',edit,name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$',remove,name='remove'),
]