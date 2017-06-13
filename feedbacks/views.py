from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from feedbacks.forms import FeedbackForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins
from django.core.mail import send_mail

class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url ='feedback'
    template_name = 'feedback.html'
    context_object_name = 'course'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,"Thank you for your feedback! We will keep in touch with you very soon!")
        return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Feedback",})
        return context
    
    mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)

# Create your views here.
