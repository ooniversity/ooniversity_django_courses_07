from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField('Name', max_length=64)
    surname = models.CharField('Surname', max_length=64)
    date_of_birth = models.DateField('Date of birth')
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=32)
    address = models.CharField('Address', max_length=128)
    skype = models.CharField('Skype', max_length=32)
    courses = models.ManyToManyField(Course, help_text='Courses')
    
    def __str__(self):
        return(self.name)
