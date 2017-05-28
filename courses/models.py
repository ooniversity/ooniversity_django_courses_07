from django.db import models
from coaches.models import Coach
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)


    def __str__ (self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=64)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__ (self):
        return self.subject

