from django import forms

class QuadraticForm(forms.Form):        
    a = forms.CharField(max_length=10, label='коэффициент a')
    b = forms.CharField(max_length=10, label='коэффициент b')
    c = forms.CharField(max_length=10, label='коэффициент c')
    
    def clean_a(self):
        data = str(self.cleaned_data['a'])
        if data == '0':
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        elif len(data) >= 2:
            if data[0] == data[1] == '-' or not data.lstrip('-').isdigit():
                raise forms.ValidationError("коэффициент не целое число")         
        return data
    
    def clean_b(self):
        data = str(self.cleaned_data['b'])
        if len(data) >= 2:
            if data[0] == data[1] == '-' or not data.lstrip('-').isdigit():
                raise forms.ValidationError("коэффициент не целое число")         
        return data

    def clean_c(self):
        data = str(self.cleaned_data['c'])
        if len(data) >= 2:
            if data[0] == data[1] == '-' or not data.lstrip('-').isdigit():
                raise forms.ValidationError("коэффициент не целое число")
        return data
