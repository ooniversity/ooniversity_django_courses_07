from django.forms import ModelForm
from students.models import Student


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        exclude = []
