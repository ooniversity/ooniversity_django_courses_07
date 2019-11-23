from django.forms import ModelForm

from .models import Course

class CourseModelForm(ModelForm):
    class Meta:
        model=Course
        fields=('name','short_description','description','coach','assistant')
