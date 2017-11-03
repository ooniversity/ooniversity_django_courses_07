'''
Created on 3 нояб. 2017 г.

@author: Roman
'''
from django.forms import ModelForm
from .models import Course, Lesson

class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
        
class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'