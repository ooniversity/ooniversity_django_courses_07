from django.contrib import admin
from coaches.models import Coach
    
class CoachAdmin(admin.ModelAdmin):
    def name(self, obj):
        return (obj.user.first_name)    

    def surname(self, obj):
        return (obj.user.last_name)    

    list_display = ['name', 'surname', 'gender', 'skype', 'description']
    list_filter = ('user__is_staff',)  


admin.site.register(Coach, CoachAdmin)
