from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('<int:coach_id>', detail,name='by_coach'),
    
]
