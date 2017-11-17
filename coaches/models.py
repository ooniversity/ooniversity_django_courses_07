from django.db import models
from django.conf import settings

# Create your models here.

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, 
        choices=(
            ('m','Male'), ('f','Female'),
        ),
    )
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)
    skype = models.CharField(max_length = 64)
    description = models.TextField()

    def __str__(self):
        return self.user.first_name

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name

   
