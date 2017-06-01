from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)

    def clean_a(self):
        data = self.cleaned_data['a']
        if data is '0':
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю.')