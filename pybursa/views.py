from django.shortcuts import render
from courses.models import Course
from django.views.generic.edit import CreateView
from feedbacks.models import Feedback
from django.urls import reverse_lazy
from django.contrib import messages
from feedbacks.forms import FeedbackForm
from django.core.mail import send_mail, mail_admins

class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback')
    form_class = FeedbackForm
    template_name = 'feedback.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        data = form.cleaned_data
        message = '{}\nMessage from {}\n{}'.format(data['message'], data['name'], data['from_email'])
        mail_admins(data['subject'], message)
        return response



def index(request):
    course_list = Course.objects.all()
    return render(request, 'index.html', {'course_list': course_list})
	
def contact(request):
	return render(request, 'contact.html')
	
def student_list(request):
	return render(request, 'student_list.html')
	
def student_detail(request):
	return render(request, 'student_detail.html')
	
def feedback(request):
	return render(request, 'feedback.html')
