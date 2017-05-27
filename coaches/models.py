from django.db import models
from django.conf import settings

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
       
    def __str__(self):
        return self.user.username
