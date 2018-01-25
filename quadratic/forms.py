from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a')
    b = forms.IntegerField(label='коэффициент b')
    c = forms.IntegerField(label='коэффициент c')

    def clean_a(self):
        a_err = self.cleaned_data['a']
        if a_err == None:
            raise forms.ValidationError("This field is required.")
        if a_err == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return a_err

    # def clean(self):
    #     cleaned_data = super(QuadraticForm, self).clean()
    #     b = cleaned_data.get("b")
    #     c = cleaned_data.get("c")
    #     if b == None:
    #         self.add_error('b',"This field is required.")
    #     if c == None:
    #         self.add_error('c',"This field is required.")







