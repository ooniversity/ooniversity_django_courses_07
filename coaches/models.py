from django.db import models
from django.contrib.auth.models import User




class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField('Date of birth', blank=True)
    gender = models.CharField(max_length=1, blank=True,
                              choices = (('M', 'Male'), ('F', 'Female')))    
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    skype = models.CharField(max_length=20, unique = True, null = True, blank=True)
    description = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.user.username
                              
# Create your models here.
