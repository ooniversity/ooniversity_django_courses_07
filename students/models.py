from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 64)
    surname = models.CharField(max_length = 64)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)
    skype = models.CharField(max_length = 64)
    courses = models.ManyToManyField('courses.Course')

    def __str__(self):
        return self.surname
