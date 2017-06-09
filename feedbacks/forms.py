from django import forms
from feedbacks.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'from_email', 'name', 'message']