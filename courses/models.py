from django.db import models

class Course(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=255)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(verbose_name='Тема', max_length=255)
    description = models.TextField(verbose_name='Описание')
    course = models.ForeignKey(Course, verbose_name='Курс')
    order = models.PositiveIntegerField(verbose_name='Номер по порядку')

    def __str__(self):
        return self.subject

