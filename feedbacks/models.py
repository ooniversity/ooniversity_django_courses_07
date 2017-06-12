from django.db import models
import datetime


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    from_email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=datetime.datetime.now())

    def __str__(self):
        return self.from_email
