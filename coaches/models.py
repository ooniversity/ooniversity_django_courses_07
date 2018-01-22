from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255, choices=[('M', 'Male'),('F' , 'Female'),])
    phone =  models.CharField(max_length=255)
    address =  models.CharField(max_length=255)
    skype =  models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.user.get_username()

    def full_name(self):
        return self.user.get_full_name()


