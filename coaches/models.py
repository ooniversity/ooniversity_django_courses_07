from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,
                              verbose_name='пользователь')
    date_of_birth=models.DateField(auto_now=False,verbose_name='краткое описание')
    gender=models.CharField(max_length=30,verbose_name='пол',choices=(
        ('M','Male'),
        ('F','Female'),
        ))
    phone=models.CharField(max_length=30,verbose_name='телефон')
    adress=models.CharField(max_length=30,verbose_name='адресс')
    skype=models.CharField(max_length=30,verbose_name='skype')
    description=models.TextField(max_length=30,verbose_name='описание')
    

    class Meta:
        verbose_name_plural='Тренеры'
        verbose_name='Тренер'

    def __str__(self):
        return self.user.first_name
    def first_name(self):
        return str(self.user.first_name)
    def last_name(self):
        return str(self.user.last_name)

