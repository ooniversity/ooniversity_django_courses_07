from django import forms
from django.core import validators


class QuadraticForm(forms.Form):        
    a = forms.CharField(label='коэффициент a', max_length=10, validators=[validators.int_list_validator('')])
    b = forms.CharField(label='коэффициент b', max_length=10, validators=[validators.int_list_validator('')])
    c = forms.CharField(label='коэффициент c', max_length=10, validators=[validators.int_list_validator('')])
       
    
    def clean_a(self):
        data = self.cleaned_data['a']
        try:
            data = int(data)
            if int(data) == 0:
                raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        except:
            raise forms.ValidationError('коэффициент не целое число')
        
        return data