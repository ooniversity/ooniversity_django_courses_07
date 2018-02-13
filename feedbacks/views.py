from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from  .forms import FeedbackForm
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    template_name = "feedback.html"
    success_url = reverse_lazy('feedback')
    form_class = FeedbackForm

    def form_valid(self, form):
        text = "Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, text)
        data = form.cleaned_data
        # mail_admins(data['subject'],data['message'])
        return super().form_valid(form)
