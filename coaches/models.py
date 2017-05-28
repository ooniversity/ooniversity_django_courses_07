from django.db import models
from django.conf import settings

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER
    )
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    description = models.TextField()

    def __str__ (self):
        return self.user.first_name