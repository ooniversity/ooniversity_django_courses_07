from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name='название')
    short_description=models.CharField(max_length=20,null=True,blank=True,
                                       verbose_name='краткое описание')
    description=models.TextField(verbose_name='полное описание')

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
    
