from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=64)  # название
    short_description = models.CharField(max_length=255) # краткое описание
    description = models.TextField() # полное описание

    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    subject = models.CharField(max_length=128)  # тема
    description = models.TextField()  # описание
    course = models.ForeignKey(Course)  # курс
    order = models.PositiveIntegerField()  # номер по порядку

    def __str__(self):
        return self.subject
