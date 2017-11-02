from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField() 
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField('courses.Course')
    
    def __str__(self):
        return ' '.join([self.surname, self.name])
    
    full_name = property(__str__)