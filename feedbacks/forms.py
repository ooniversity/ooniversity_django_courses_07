'''
Created on 3 нояб. 2017 г.

@author: Roman
'''
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['create_date']