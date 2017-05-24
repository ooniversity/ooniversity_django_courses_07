from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    adress = models.CharField(max_length=25)
    skype = models.CharField(max_length=25)
    # courses

    def __str__(self):
        return self.name + " " + self.surname
