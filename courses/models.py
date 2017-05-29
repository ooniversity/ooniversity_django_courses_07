from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, related_name='coach_courses', blank=True)
    assistant = models.ForeignKey(Coach, null=True, related_name='assistant_courses', blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
