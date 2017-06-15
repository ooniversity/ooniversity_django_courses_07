from django import forms
from students.models import Student


class StudentModelForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"  # to avoid ImproperlyConfigured error
        #exclude = []
        





       
