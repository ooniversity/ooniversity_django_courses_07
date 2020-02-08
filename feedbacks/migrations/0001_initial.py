# Generated by Django 2.2.5 on 2019-12-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя отправителя')),
                ('subject', models.CharField(max_length=30, verbose_name='тема')),
                ('message', models.TextField(verbose_name='сообщение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('from_email', models.EmailField(max_length=254, verbose_name='почта отправителя')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
