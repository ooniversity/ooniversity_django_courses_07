from .models import Course, Lesson
from django.forms import ModelForm

class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
