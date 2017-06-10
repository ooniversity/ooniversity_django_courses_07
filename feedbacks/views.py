from django.shortcuts import render
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        send_mail(form.instance.subject, form.instance.message, form.instance.from_email, settings.ADMINS, fail_silently=False)
        return response

