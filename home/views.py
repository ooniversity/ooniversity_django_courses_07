from django.shortcuts import render
from courses.models import Course

def home_page(request):
    all_courses=Course.objects.all()
    context={'courses':all_courses}
    return render(request,'home/home.html',context)
        
    
