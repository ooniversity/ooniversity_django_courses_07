from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="имя отправителя")
    subject = models.CharField(max_length=255, verbose_name="тема сообщения")
    message = models.TextField(verbose_name="текст сообщения")
    from_email = models.EmailField(verbose_name="email отправителя")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="дата и время создания")

    def __str__(self):
        return self.name

