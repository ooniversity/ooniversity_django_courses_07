from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'short_description', 'description', 'coach', 'assistant']


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'description', 'course', 'order']
