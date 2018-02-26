from django import forms

class QuadraticForm(forms.Form):        
    a = forms.CharField(max_length=10, label='коэффициент a')
    b = forms.CharField(max_length=10, label='коэффициент b')
    c = forms.CharField(max_length=10, label='коэффициент c')
    
    def clean_a(self):
        data = self.cleaned_data['a']
        if data == '':
            raise forms.ValidationError("This field is required.")
        elif data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        elif isinstance(data, str):
            if data not in '-0123456789':
                raise forms.ValidationError("коэффициент не целое число")         
        return data
    
    def clean_b(self):
        data = self.cleaned_data['b']
        if data == '':
            raise forms.ValidationError("This field is required.")
        elif isinstance(data, str):
            if data not in '-0123456789':
                raise forms.ValidationError("коэффициент не целое число")         
        return data

    def clean_c(self):
        data = self.cleaned_data['c']
        if data == '':
            raise forms.ValidationError("This field is required.")
        elif isinstance(data, str):
            if data not in '-0123456789':
                raise forms.ValidationError("коэффициент не целое число")         
        return data
