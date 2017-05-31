from django.db import models
from courses.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True,blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

    def full_name_field(self ):
        return self.name+' '+self.surname
    full_name_field.short_description = "Full name"
    fullname = property(full_name_field)

