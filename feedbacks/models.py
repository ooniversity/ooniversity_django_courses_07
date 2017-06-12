from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)
