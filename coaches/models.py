from django.db import models
from django.conf import settings

# Create your models here.


class Coach(models.Model):

    date_of_birth = models.DateField
    gender =  models.CharField(max_length=1,choices=(('m','Male'), ('f','Female')))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.user
