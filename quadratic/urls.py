from django.conf.urls import url

from . import views


urlpatterns = [
    #url(r'^results/a=(?P<a>\d+)&b=(?P<b>\d+)&c=(?P<c>\d+)$',views.results,name="results"),
    url(r'^results/$',views.quadratic_results,name="results"),
]