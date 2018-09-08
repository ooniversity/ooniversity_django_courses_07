from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.core.mail import send_mail


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        #send_mail(self.object.subject, 
        #          self.object.message,
        #          self.object.from_email, 
        #          ['localhost'], 
        #          fail_silently=False)
        return response

    def get_success_url(self):
        return reverse('feedback')


