from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.core.mail import mail_admins
from .models import Feedback
from .forms import FeedbackForm

class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Обратная связь'
        return context

    def form_valid(self, form):
        messages.success(self.request,"Thank you for your feedback! We will keep in touch with you very soon!")
        instance = form.cleaned_data()
        mail_admins(instance['subject'],instance['message'])
        return super().form_valid(form)