from django.db import models
from coaches.models import Coach
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

