from django.db import models

class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    short_description = models.CharField(verbose_name='Short description', max_length=255)
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(verbose_name='Subject', max_length=255)
    description = models.TextField(verbose_name='Description')
    course = models.ForeignKey(Course, verbose_name='Course')
    order = models.PositiveIntegerField(verbose_name='Order')

    def __str__(self):
        return self.subject

