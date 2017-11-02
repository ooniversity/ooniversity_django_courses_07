from django import forms
from django.core.exceptions import ValidationError


def validate_all(value):
    try:
        value = int(value)
    except:
        raise ValidationError('коэффициент не целое число')

class QuadraticForm(forms.Form):        
    a = forms.CharField(label='коэффициент a', max_length=10, validators=[validate_all])
    b = forms.CharField(label='коэффициент b', max_length=10, validators=[validate_all])
    c = forms.CharField(label='коэффициент c', max_length=10, validators=[validate_all])
       
    
    def clean_a(self):
        data = self.cleaned_data['a']
        if int(data) == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        
        return data