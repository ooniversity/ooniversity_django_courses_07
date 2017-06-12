from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ['Full_name', 'email', 'skype']
	list_display_links = ['Full_name']
	list_filter = ['courses']
	search_fields = ['surname', 'email']
	filter_horizontal = ['courses']

	def Full_name(self, obj):
	    return obj.name + ' ' + obj.surname
	    
	fieldsets = [
		('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
		('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
		(None, {'fields': ['courses']}),
	]    
    
admin.site.register(Student, StudentAdmin)