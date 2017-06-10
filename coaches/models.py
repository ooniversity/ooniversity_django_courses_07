from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def full_name(self):
        return self.user.get_full_name()
