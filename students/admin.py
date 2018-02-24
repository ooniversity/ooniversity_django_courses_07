from django.contrib import admin
from students.models import Student

def fullname(obj):
    obj.short_description = 'Full name'
    return ("%s %s" % (obj.name, obj.surname))

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname']
    list_display = [fullname, 'email', 'skype']
    list_filter = ['courses']    
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
                 (None, {'fields': ['courses']})]
    
    #formfield_overrides = 

admin.site.register(Student, StudentAdmin)
