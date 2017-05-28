from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(User)
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
        return self.user.username

    def field_name(self):
        return self.user.first_name

    name = property(field_name)

    def field_surname(self):
        return self.user.last_name

    surname = property(field_surname)