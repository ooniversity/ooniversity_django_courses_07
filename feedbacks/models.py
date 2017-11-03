from django.db import models

# Create your models here.
class Feedback(models.Model):
    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now=True)