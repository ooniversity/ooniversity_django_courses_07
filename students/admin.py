from django.contrib import admin
from students.models import Student



class StudentAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'full name': ('name', 'surname',), }
    admin.site.site_header = "PyBursa Administration"
    list_display = ( 'get_full_name','email','skype')
    search_fields = ['surname','email', ]
    list_filter = ['courses',]

    fieldsets = (( "Personal info",
                  {'fields': ('name', 'surname', 'date_of_birth')}),
                 ('Contact info',
                  {'classes': ('wide',),
                   'fields': ('email', 'phone','address','skype', 'courses')}),

                 )


admin.site.register(Student, StudentAdmin)

