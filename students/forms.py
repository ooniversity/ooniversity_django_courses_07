from django.forms import ModelForm
from .models import Student

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
