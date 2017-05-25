from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=128)
    short_description = models.CharField(max_length=254)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length=254)
    description = models.TextField()
    course = models.ForeignKey(Course, null=True)
    order = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.subject

