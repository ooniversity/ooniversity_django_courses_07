from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F','Female')
    )

    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
