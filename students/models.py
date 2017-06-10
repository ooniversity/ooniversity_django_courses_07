from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=254)
    skype = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name + ' ' + self.surname

    def fullname(self):
        return self.surname + ' ' + self.name

    def get_courses(self):
        return self.courses.all()

    def reformat_birthdate(self):
        return self.date_of_birth.strftime("%b. %d, %Y")
