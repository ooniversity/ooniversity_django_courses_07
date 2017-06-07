from django import forms

class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10, label="коэффициент a", required=True)
    b = forms.CharField(max_length=10, label="коэффициент b", required=True)
    c = forms.CharField(max_length=10, label="коэффициент c", required=True)

    def clean_a(self):
        a = self.cleaned_data['a']
        try:
            a = int(a)
        except:
            raise forms.ValidationError('коэффициент не целое число')
        if a == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return a
