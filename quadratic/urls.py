from django.conf.urls import url,include
from  . import  views

urlpatterns = [
    url(r'^results/$',views.quadratic_results,name='results')
]