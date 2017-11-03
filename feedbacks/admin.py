from django.contrib import admin
from .models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']

admin.site.register(Feedback, FeedbackAdmin)