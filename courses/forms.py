from django import forms
from .models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
