from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(label='коэффициент a', max_length=5, required=True)
    b = forms.CharField(label='коэффициент b', max_length=5)
    c = forms.CharField(label='коэффициент c', max_length=5)

    def is_integer(self, a):
        """
        Return True if "a" is integer, else Return False 

        """
        try:
            int(a)
            return True
        except ValueError:
            return False

    def clean_a(self):
        data = self.cleaned_data['a']
        print(data)
        if data == '0':
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        elif not self.is_integer(data):
            raise forms.ValidationError("коэффициент не целое число")
        return data

    def clean_b(self):
        data = self.cleaned_data['b']
        print(data)
        if not self.is_integer(data):
            raise forms.ValidationError("коэффициент не целое число")
        return data

    def clean_c(self):
        data = self.cleaned_data['c']
        print(data)
        if not self.is_integer(data):
            raise forms.ValidationError("коэффициент не целое число")
        return data