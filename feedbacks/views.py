from django.core.mail import mail_admins, send_mail, send_mass_mail
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbackView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'

    def form_valid(self, form):
        from_email = form.cleaned_data['from_email']
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message'] + '\n\nСообщение от ' + name + '\n' + from_email
        mail_admins(subject, message)
        return super(FeedbackView, self).form_valid(form)
