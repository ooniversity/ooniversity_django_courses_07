from django.shortcuts import render
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, mail_admins
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')
    template_name = 'feedback.html'

    def form_valid(self, form):
        message_to_admins = 'From: ' + form.cleaned_data['name'] + '(' +form.cleaned_data['from_email'] + ')\n' + form.cleaned_data['subject'] + '\n' + form.cleaned_data['message']
        mail_admins('Feedback', message_to_admins)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super(FeedbackView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Leave a feedback"
        return context
