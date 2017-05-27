from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course)

    def __str__ (self):
        return self.name

    def fullname_field(self):
        return self.name + ' ' + self.surname

    fullname_field.short_description = "Full name"

    fullname = property(fullname_field)
