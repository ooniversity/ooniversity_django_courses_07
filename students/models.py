from django.db import models
from courses.models import Course

class Student(models.Model):
    name=models.CharField(max_length=50,verbose_name='имя')
    surname=models.CharField(max_length=50,verbose_name='фамилия')
    date_of_birth=models.DateField(verbose_name='дата рождения')
    email=models.EmailField(verbose_name='почта')
    phone=models.CharField(max_length=20,verbose_name='телефон')
    adress=models.CharField(max_length=50,verbose_name='адрес')
    skype=models.CharField(max_length=50,verbose_name='скайп')
    courses=models.ManyToManyField(Course,null=True)

    class Meta:
        verbose_name_plural='Студенты'
        verbose_name='Студент'
        

    def __str__(self):
        return self.surname
    


