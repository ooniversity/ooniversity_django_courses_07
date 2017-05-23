from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=64)  # имя
    surname = models.CharField(max_length=64)  # фамилия
    date_of_birth = models.DateField()  # дата рождения
    email = models.EmailField()
    phone = models.CharField(max_length=32)  # телефон
    address = models.CharField(max_length=255) # адрес
    skype = models.CharField(max_length=32)
    courses = models.ManyToManyField(Course)  # курсы, на которых учится студент