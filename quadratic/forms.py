from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a',
                           error_messages={'required': 'This field is required.'})
    b = forms.IntegerField(label='коэффициент b',
                           error_messages={'required': 'This field is required.'})
    c = forms.IntegerField(label='коэффециент c',
                           error_messages={'required': 'This field is required.'})

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return a



