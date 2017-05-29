from django.db import models
from django.conf import settings


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,
                              choices=(
                                  ('M', 'Male'),
                                  ('F', 'Female'),
                                )
                              )
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


