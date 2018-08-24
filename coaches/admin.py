from django.contrib import admin
from .models import Coach


class CoachAdmin(admin.ModelAdmin):
    
    def first_name(self, obj):
        #print(obj.user.is_staff)
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name

    #def staff_filter(self, obj):
    #    print(obj.user.is_staff)

    list_display = ["first_name", "last_name", "gender", "skype", "description"]
    list_filter = ["user"]

    #list_filter = (
    #    ("user.is_staff", admin.BooleanFieldListFilter),
    #)

admin.site.register(Coach, CoachAdmin)
