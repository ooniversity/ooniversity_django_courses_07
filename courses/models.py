from django.db import models
from coaches.models import Coach

class Course(models.Model):
  name = models.CharField(max_length=200)
  short_description = models.CharField(max_length=255)
  description = models.TextField()
  coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
  assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')
  
  def __str__(self):
    return self.name
  
class Lesson(models.Model):
  subject = models.CharField(max_length=50)
  description = models.TextField()
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  order = models.PositiveIntegerField()
  
  def __str__(self):
    return self.subject
    

# Create your models here.
