from django.urls import path

from .views import by_course,CourseAddView
from .views import CourseUpdateView,CourseDeleteView,LessonAddView

urlpatterns = [
    path('<int:course_id>/',by_course,name='by_course'),
    path('<int:course_id>/add_lesson',LessonAddView.as_view(),name='add_lesson'),
    path('add/',CourseAddView.as_view(),name='add_course'),
    path('edit/<int:course_id>/',CourseUpdateView.as_view(),name='edit_course'),
    path('remove/<int:course_id>/',CourseDeleteView.as_view(),name='remove_course'),
    
    ]
