from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',course_list,name='student_list'),
    path('<int:student_id>',student_detail,name='by_student'),
]
