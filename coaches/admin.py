from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description' )
    search_fields = ['user', 'user__first_name', 'user__last_name', 'user_email', 'skype', 'gender', ]
    list_filter = ['gender', 'user__is_staff',]  

  

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name

   
    
admin.site.register(Coach, CoachAdmin)
# Register your models here.
