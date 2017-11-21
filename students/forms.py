from django.forms import ModelForm, widgets, DateInput
from .models import Student

class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput
            }
