from django.db import models
from courses.models import Course
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=timezone.now)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

    def get_full_name(self):
        return u'%s %s' %( self.name, self.surname)

    get_full_name.short_description = 'full name'