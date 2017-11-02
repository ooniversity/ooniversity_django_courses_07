from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', "Male"), ('F', 'Female')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    skype = models.CharField(max_length=100)
    description = models.TextField()

    
    def __str__(self):
        return self.user.get_username()
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name