from django.conf.urls import url
from students import views

app_name = 'students'
urlpatterns = (
    url(r'^$', views.StudentsListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.StudentsDetailView.as_view(), name='detail'),
    url(r'^add/$', views.StudentsCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentsUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentsDeleteView.as_view(), name='remove'),
)