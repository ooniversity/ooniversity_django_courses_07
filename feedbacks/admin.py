from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    search_fields = ('name', 'from_email')
    list_display = ['from_email', 'create_date']
    list_filter = ['create_date']


admin.site.register(Feedback, FeedbackAdmin)
