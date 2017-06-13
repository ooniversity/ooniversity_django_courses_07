from django.contrib import admin
from feedbacks.models import Feedback



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'create_date',)
    exclude = []

    
    

admin.site.register(Feedback, FeedbackAdmin)
admin.site.site_header = 'PyBursa Administration'

# Register your models here.
