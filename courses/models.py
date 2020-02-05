from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=256)
    description = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
