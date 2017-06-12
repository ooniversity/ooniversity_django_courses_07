from django.contrib import admin
from .models import Coach

class CoachAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description' )
    # list_display = ('__unicode__',)
    # list_display = ('user',)  # 'user_last_name', 'user_first_name'

    search_fields = ['user', 'user__first_name', 'user__last_name', 'user_email', 'skype', 'gender', ]
    list_filter = ['gender', 'user__is_staff', ]  # exceeds min reqs

    def first_name(self, obj): return obj.user.first_name
    def last_name(self, obj): return obj.user.last_name

admin.site.register(Coach, CoachAdmin)

