from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',StudentListView.as_view(),name='student_list'),
    path('add/',StudentCreateView.as_view(),name='add_student'),
    path('edit/<int:student_id>',StudentUpdateView.as_view(),name='edit_student'),
    path('remove/<int:student_id>',StudentDeleteView.as_view(),name='remove_student'),
    path('<int:student_id>',StudentDetailView.as_view(),name='by_student'),
]
