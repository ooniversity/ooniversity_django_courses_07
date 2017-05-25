from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фамилия', max_length=255)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField()
    phone = models.CharField(verbose_name='Контактный телефон', max_length=20)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    skype = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course, verbose_name='Курсы')

    def __str__(self):
        full_name = self.name + ' ' + self.surname
        return full_name