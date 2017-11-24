
from django.conf.urls import include, url
from feedbacks import views
app_name = 'feedbacks'
urlpatterns = [
    url(r'^$', views.FeedbackView.as_view(), name = 'feedback'),
]
   
