from django.shortcuts import render
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin


class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    #form_class = FeedbackForm
    fields = ['name', 'subject', 'message', 'from_email']
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(form.instance.subject, form.instance.message, form.instance.from_email, settings.ADMINS, fail_silently=False)
        return response

