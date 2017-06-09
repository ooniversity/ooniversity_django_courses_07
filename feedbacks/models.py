from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject