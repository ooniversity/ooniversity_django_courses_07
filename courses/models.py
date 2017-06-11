from django.db import models
from coaches.models import Coach
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=128)
    short_description = models.CharField(max_length=254)
    description = models.TextField(null=True)

    coach = models.ForeignKey(Coach, null=True, blank=True,
                                                on_delete=models.CASCADE,
                                                related_name="coach_courses")
    assistant = models.ForeignKey(Coach, null=True, blank=True,
                                                on_delete=models.CASCADE,
                                                related_name="assistant_courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:edit', kwargs={'pk': self.pk})


class Lesson(models.Model):
    subject = models.CharField(max_length=254)
    description = models.TextField()
    course = models.ForeignKey(Course, null=True)
    order = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.subject

