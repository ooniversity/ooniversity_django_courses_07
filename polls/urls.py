from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
	url(r'^polls/latest\.html$',views.index),
	url(r'^specifics/(?P<quetion_id>[0-9]+)/$',views.detail,name ='detail'),
]

