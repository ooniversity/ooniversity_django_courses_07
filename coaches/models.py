from django.db import models
from django.conf import settings

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField('Date of birth')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField('Phone', max_length=32)
    address = models.CharField('Address', max_length=128)
    skype = models.CharField('Skype', max_length=32)
    description = models.TextField()
    
    def __str__(self):
        return(self.user.username)
