from django.db import models
from courses.models import Course

class Student(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  email = models.EmailField(max_length=70)
  phone = models.CharField(max_length=15)
  address = models.CharField(max_length=120)
  skype = models.CharField(max_length=50)
  courses = models.ManyToManyField(Course)
  
  def __str__(self):
    return '%s %s' % (self.name, self.surname)

  def fullname(self):
    return self.name +" " + self.surname
  
  def get_courses(self):
    return self.courses.all()

  def birthdate_format(self):
     return self.date_of_birth.strftime("%b. %d, %Y")
# Create your models here.
