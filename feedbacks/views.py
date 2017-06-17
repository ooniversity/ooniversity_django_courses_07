from django.shortcuts import render, redirect, get_object_or_404
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url ='feedback'
    template_name = 'feedback.html'    
    
    def form_valid(self, form):
        response = super(FeedbackView, self).form_valid(form)
        messages.success(self.request,"Thank you for your feedback! We will keep in touch with you very soon!")
        data = form.cleaned_data
        message = '{}\nMessage from {}\n{}'.format(data['message'], data['name'], data['from_email'])
        mail_admins(data['subject'], message)
        return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title':"Feedback",})
        return context
    
    
# Create your views here.
