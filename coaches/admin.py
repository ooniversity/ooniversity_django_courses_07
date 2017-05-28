from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['First_name', 'Last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']
    
    def First_name(self, obj):
        return obj.user.first_name
        
    def Last_name(self, obj):
        return obj.user.last_name
        
admin.site.register(Coach, CoachAdmin)


# Register your models here.
