from django.views.generic import CreateView
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.core.mail import mail_admins
from django.urls import reverse_lazy


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedbacks')

    def form_valid(self, form):
        response = super().form_valid(form)
        mess = 'Name: %s \n Subject: %s \n Message  : %s \n From : %s \n ' % \
               (self.object.name, self.object.subject, self.object.message, self.object.from_email)
        mail_admins('New feedback', mess)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response

