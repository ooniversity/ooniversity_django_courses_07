from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name='Student name', max_length=255)
    surname = models.CharField(verbose_name='Student surname', max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)
