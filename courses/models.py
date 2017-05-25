from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')


    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
