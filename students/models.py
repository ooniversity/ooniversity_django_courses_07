from django.db import models
from courses.models import Course
# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=32)
	surname = models.CharField(max_length=32)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=32)
	address = models.CharField(max_length=64)
	skype = models.CharField(max_length=32)
	course = models.ManyToManyField(Course)
	
	def __str__(self):
		return self.name + ' ' + self.surname