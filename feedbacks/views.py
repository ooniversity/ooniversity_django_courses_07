from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        feedback_message = ("New feedback from: %s(%s)" % (form.instance.name, form.instance.from_email))
        mail_admins('Feedback', feedback_message)
        return super().form_valid(form)
