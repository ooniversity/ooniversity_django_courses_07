from django.views import generic
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from feedbacks.models import Feedback

class FeedbackView(SuccessMessageMixin, generic.CreateView):
    model = Feedback
    fields = '__all__'
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'
    
    def form_valid(self, form):
        responce = super().form_valid(form)
        send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], form.cleaned_data['from_email'], settings.ADMINS)
        return responce
