
from django.contrib import admin
from django.urls import path,include
from feedbacks.views import FeedbackView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quadratic/',include('quadratic.urls')),
    path('',include('home.urls')),
    path('courses/',include('courses.urls')),
    path('students/',include('students.urls')),
    path('coaches/',include('coaches.urls')),
    path('feedback/',FeedbackView.as_view(),name='feedback'),
     
]
