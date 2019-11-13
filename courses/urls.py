from django.urls import path

from .views import by_course

urlpatterns = [
    path('<int:course_id>/',by_course,name='by_course'),
    ]
