from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic import CreateView

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.

class FeedbackView(CreateView):
    model = Feedback
    form = FeedbackForm
    fields = '__all__'
    success_url = reverse_lazy('feedback')
    template_name = 'feedback.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        try: 
            mail_admins(self.object.subject, self.object.message)
            print('ok')
        except:
            print('error')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Обратная связь'
        return context
