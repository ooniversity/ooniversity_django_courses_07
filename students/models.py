from django.db import models
from courses.models import Course



class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_of_birth = models.DateField('Date of birth', blank=True)
    email = models.EmailField(max_length=20, unique = True)
    phone = models.CharField(max_length=20, unique = True,  blank=True)
    address = models.CharField(max_length=40, null = True, blank=True)
    skype = models.CharField(max_length=20, unique = True, null = True, blank=True)
    courses = models.ManyToManyField(Course)    

    def __str__(self):
        return u'{} {}'.format(self.name, self.surname)

# Create your models here.
