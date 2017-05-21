from django.conf.urls import url,include
from  . import  views

urlpatterns = [
    url(r'^result/$',views.quadratic_results,name='results')
]