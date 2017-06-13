from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=100, null = True, blank=True)
    message = models.TextField(null = True, blank=True)
    from_email = models.EmailField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'{} {}'.format(self.name, self.create_date)

# Create your models here.
