from django.contrib import admin
from feedbacks.models import Feedback


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']


admin.site.register(Feedback, FeedbacksAdmin)
