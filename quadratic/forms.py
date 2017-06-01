from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(localize=True, label='коэффициент a')
    b = forms.IntegerField(localize=True, label='коэффициент b')
    c = forms.IntegerField(localize=True, label='коэффициент c')

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return a