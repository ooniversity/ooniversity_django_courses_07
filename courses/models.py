from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name