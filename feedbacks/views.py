from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
class FeedbackView(CreateView):
    
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('feedback')
    
    def form_valid(self, form):
        if settings.ADMINS:
            recipients = []
            for item in settings.ADMINS:
                recipients.append(item[1])
                
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['from_email'],
                recipients,
                fail_silently=False
            )
                
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        
        return super().form_valid(form)