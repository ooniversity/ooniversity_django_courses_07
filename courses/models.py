from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=200)
    description = models.TextField(null = True)

    def __str__(self):
        return self.name
        

class Lesson(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField(max_length=200)
    course = models.ForeignKey('Course')
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.subject
    
