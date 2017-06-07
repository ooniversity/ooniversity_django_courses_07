from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    skype = models.CharField(max_length=150)
    courses = models.ManyToManyField(Course)


    def fullname(self):
        return self.name + ' ' + self.surname
    full_name = property(fullname)





