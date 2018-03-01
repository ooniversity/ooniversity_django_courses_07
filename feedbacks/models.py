from django.db import models

class Feedback(models.Model):
    name = models.CharField('Имя отправителя', max_length=64) 
    subject = models.CharField('Тема сообщения', max_length=256)
    message = models.TextField('Сообщение')
    from_email = models.EmailField('Email отправителя')
    create_date = models.DateTimeField('Дата и время отправки', auto_now_add=True)
    
    def __str__(self):
        return self.name
