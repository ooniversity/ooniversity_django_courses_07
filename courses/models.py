from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name='название')
    short_description=models.CharField(max_length=20,null=True,blank=True,
                                       verbose_name='краткое описание')
    description=models.TextField(verbose_name='полное описание')
    coach=models.ForeignKey(Coach,on_delete=models.CASCADE,
                            related_name='coach_courses',verbose_name='тренер',
                            null=True,blank=True)
    assistant=models.ForeignKey(Coach,on_delete=models.CASCADE,
                            related_name='assistant_courses',
                            verbose_name='помощник',null=True,blank=True)

    

    class Meta:
        verbose_name_plural='Курсы'
        verbose_name='Курс'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject=models.CharField(max_length=30,verbose_name='тема')
    course=models.ForeignKey(Course,on_delete=models.PROTECT)
    description=models.TextField(verbose_name='описание')
    order=models.PositiveIntegerField(verbose_name='номер по порядку')

    class Meta:
        verbose_name_plural='Уроки'
        verbose_name='Урок'
        ordering=['order']

    def __str__(self):
        return self.subject
    
