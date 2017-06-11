from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=16)
    subject = models.CharField(max_length=32)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    