from django.contrib import messages
from django.urls import reverse
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        email_message = 'Name: %s /n Subject: %s /n Message: %s /n From email: %s' % \
                        (self.object.name, self.object.subject, self.object.message, self.object.from_email)
        mail_admins('new feedback', email_message)
        return response

    def get_success_url(self):
        return reverse('feedback')


