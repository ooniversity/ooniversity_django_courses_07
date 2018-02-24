from django.db import models

class Course(models.Model):
    name = models.CharField('Название', max_length=64)
    short_description = models.CharField('Краткое описание', max_length=256)
    description = models.CharField('Подробное описание', max_length=512)
    
    def __str__(self):
        return(self.name)
        
class Lesson(models.Model):
    subject = models.CharField('Тема', max_length=128)
    description = models.TextField('Описание')
    course = models.ForeignKey(Course, help_text='Курс')
    order = models.PositiveIntegerField('Номер по порядку')    
        
    def __str__(self):
        return(self.subject)
