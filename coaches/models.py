from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(verbose_name='Пол', choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
    phone = models.CharField(verbose_name='Телефон', max_length=15)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    skype = models.CharField(max_length=20)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.user.first_name

    def name(self):
        return self.user.first_name

    def surname(self):
        return self.user.last_name

    def is_stuff(self):
        return self.user.is_staff
