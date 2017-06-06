from django.db import models
from courses.models import Course
from django.core.urlresolvers import reverse


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    def get_absolute_url(self):
        return reverse('students:list_view')

    def __str__(self):
        return self.name + ' ' + self.surname