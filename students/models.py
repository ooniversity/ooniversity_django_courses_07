from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    courses = models.ManyToManyField(to=Course)
