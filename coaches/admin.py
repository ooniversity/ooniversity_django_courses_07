from django.contrib import admin
from  .models import Coach
# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user','gender','skype','description']


admin.site.register(Coach)
