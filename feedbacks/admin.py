from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']
    search_fields = ['from_email']


admin.site.site_header = 'PyBursa Administration'
admin.site.register(Feedback, FeedbackAdmin)