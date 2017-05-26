from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices = (('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.user


    def user_name(self):
        return self.user.first_name
    name = property(user_name)


    def user_surname(self):
        return self.user.last_name
    surname = property(user_surname)

