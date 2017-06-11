from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm



class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    context_object_name = 'feedback'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        feedback = form.cleaned_data
        mail_admins(feedback.get('subject'), feedback.get('message'),fail_silently=False)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return super().form_valid(form)

# Create your views here.
