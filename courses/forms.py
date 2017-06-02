from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonModelForm(forms.ModelForm):
    order = forms.IntegerField(localize=True)

    class Meta:
        model = Lesson
        fields = '__all__'