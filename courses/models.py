from django.db import models
from coaches.models import Coach

class Course(models.Model):
    name = models.CharField('Name', max_length=64)
    short_description = models.CharField('Short description', max_length=256)
    description = models.TextField('Description')
    coach = models.ForeignKey(Coach, related_name='coach_courses', null=True, blank=True)
    assistant = models.ForeignKey(Coach, related_name='assistant_courses', null=True, blank=True)
    
    def __str__(self):
        return(self.name)
        
class Lesson(models.Model):
    subject = models.CharField('Subject', max_length=128)
    description = models.TextField('Description')
    course = models.ForeignKey(Course, help_text='Course')
    order = models.PositiveIntegerField('Order')    
        
    def __str__(self):
        return(self.subject)
