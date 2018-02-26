from django import forms

class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10, label='коэффициент a', error_messages={'required': 'This field is required.'})
    b = forms.CharField(max_length=10, label='коэффициент b', error_messages={'required': 'This field is required.'})
    c = forms.CharField(max_length=10, label='коэффициент c', error_messages={'required': 'This field is required.'})
