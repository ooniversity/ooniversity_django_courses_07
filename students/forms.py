from django import forms 
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','surname','date_of_birth','email','phone',
                'adress','skype','courses')
