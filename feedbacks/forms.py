from django.db import models
from django.conf import settings
from django import forms
from feedbacks.models import Feedback


class FeedbackForm (forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'subject', 'message',
                  'from_email']
        


       
