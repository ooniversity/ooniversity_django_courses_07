from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10, label='коэффициент a')
    b = forms.CharField(max_length=10, label='коэффициент b')
    c = forms.CharField(max_length=10, label='коэффициент c')

    def clean_a(self):
        data = self.cleaned_data['a']
        if data is '0':
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю.')