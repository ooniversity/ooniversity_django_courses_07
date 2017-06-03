from django import forms

class QuadraticForm(forms.Form):
    a = forms.CharField(max_lenght = 100)
    b = forms.CharField(max_lenght = 100)
    c = forms.CharField(max_lenght = 100)