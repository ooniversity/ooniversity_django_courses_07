from django.db import models
from courses.models import Course


class Student(models.Model):
	name = models.CharField(max_length=150)
	surname = models.CharField(max_length=150)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=150)
	address = models.CharField(max_length=300)
	skype = models.CharField(max_length=150)
	courses = models.ManyToManyField(Course)


	def fullname(self):
		return self.name + ' ' + self.surname
	full_name = property(fullname)

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
#	def __unicode__(self):
#		return "{0}".format(self.title)

#	def __str__(self):
#		return self.name
# Create your models here.
