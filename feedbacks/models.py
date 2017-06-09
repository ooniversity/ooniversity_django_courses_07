from django.db import models


class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    from_email = models.EmailField()
    name = models.CharField(max_length=50)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now=True, editable=False)