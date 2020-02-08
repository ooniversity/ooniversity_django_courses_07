from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=50,verbose_name='имя отправителя')
    subject=models.CharField(max_length=30,verbose_name='тема')
    message=models.TextField(verbose_name='сообщение')
    create_date=models.DateTimeField(verbose_name='дата создания',auto_now_add=True)
    from_email=models.EmailField(verbose_name='почта отправителя')
   

    class Meta:
        verbose_name_plural='Отзывы'
        verbose_name='Отзыв'
        

    def __str__(self):
        return self.name
