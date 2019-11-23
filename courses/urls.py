from django.urls import path

from .views import by_course,CourseAddView

urlpatterns = [
    path('<int:course_id>/',by_course,name='by_course'),
    path('add/',CourseAddView.as_view(),name='add_course'),
    #path('edit/<int:course_id>/',edit,name='edit_course'),
    #path('remove/<int:course_id>/',remove,name='remove_course'),
    
    ]
