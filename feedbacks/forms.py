from django import forms
from feedbacks.models import Feedback

class CourseModelForm (forms.ModelForm):        
    class Meta:
        model = Feedback
        fields = '__all__'
