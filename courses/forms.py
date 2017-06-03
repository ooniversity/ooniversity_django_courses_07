from django import forms
from courses.models import Course,Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model=Course
        exclude=['']

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"