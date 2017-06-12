from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse

class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:edit', kwargs={'pk': self.pk})
    
         
class Lesson(models.Model):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.subject
    
