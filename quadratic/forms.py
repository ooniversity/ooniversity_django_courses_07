from django import forms



class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a')
    b = forms.IntegerField(label='коэффициент b')
    c = forms.IntegerField(label='коэффициент c')

    # Валидация проходит в этом методе
    #def clean(self):
        # Определяем правило валидации
        #if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            #raise forms.ValidationError('Пароли должны совпадать!')
        #return self.cleaned_data

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
  # Always return the cleaned data, whether you have changed it or
        # not.
        return data

  #def clean(self):
        #if not self._errors:
            #cleaned_data = super(QuadraticForm, self).clean()
        #return cleaned_data

   

