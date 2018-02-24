from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField('Имя', max_length=64)
    surname = models.CharField('Фамилия', max_length=64)
    date_of_birth = models.DateField('Дата рождения')
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=32)
    address = models.CharField('Адрес', max_length=128)
    skype = models.CharField(max_length=32)
    courses = models.ManyToManyField(Course, help_text='Курсы, на которых учится студент')
    
    def __str__(self):
        return(self.name)
