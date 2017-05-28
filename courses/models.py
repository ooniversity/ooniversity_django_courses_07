from django.db import models
from django.conf import settings

class Course(models.Model):
	name = models.CharField(max_length=255, null=True)
	short_description = models.CharField(max_length=255, null=True)
	description = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length=255, null=True)
	description = models.TextField(max_length=255, null=True)
	course = models.ForeignKey(Course)
	order = models.PositiveIntegerField()

	def __str__(self):
		return self.name

#class Student(models.Model):
#	name = models.CharField(max_length=255, null=True)
#	surname = models.CharField(max_length=255, null=True)
#	date_of_birth = models.DateField(null=True, blank=True)	
#	email = models.EmailField(unique=True, null=True)
#	phone = models.CharField(max_length=255, null=True)
#	adress = models.CharField(max_length=255, null=True)
#	skype = models.CharField(max_length=255, null=True)
#	courses = models.ManyToManyField(Course)
#	def get_courses(self):
#		return ",".join([str(p) for p in self.courses.all()])
#
#	def __unicode__(self):
#		return "{0}".format(self.title)
#
#	def __str__(self):
#		return self.name
# Create your models here.
