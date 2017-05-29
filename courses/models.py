from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=64)
    description = models.TextField(max_length=2000)
    def __str__(self):
    	return self.name

class Lesson(models.Model):
    order = models.PositiveIntegerField()
    subject = models.CharField(max_length=64)
    description = models.TextField(max_length=2000)
    courses = models.ForeignKey(Course)
    def __str__(self):
    	return self.subject