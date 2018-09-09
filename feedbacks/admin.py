from django.contrib import admin
from feedbacks.models import Feedback
from django.db import models
from django.forms import widgets


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']


admin.site.register(Feedback, FeedbackAdmin)
    
