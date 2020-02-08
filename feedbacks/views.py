from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import mail_admins

class FeedbackView(CreateView):
    model=Feedback
    form_class=FeedbackForm
    template_name='feedback.html'
    success_url=reverse_lazy('feedback')

    def form_valid(self,form):
        messages.success(self.request,
                         'Thank you for your feedback!\
                        We will keep in touch with you very soon!')
        subject=form.instance.subject
        message=form.instance.message
        email=form.instance.from_email
        mail_admins(subject,message)
        return super().form_valid(form)

