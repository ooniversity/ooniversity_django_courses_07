from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=25)
    description = models.TextField()
    # course
    # order

    def __str__(self):
        return self.subject

