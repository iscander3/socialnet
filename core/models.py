from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 55)
    description = models.TextField(null=True, blank=True)


class Post(models.Model):
    STATUS_CHOICES = (
        ('Опубликован', 'Опубликован'),
        ('Не опубликован', 'Не опубликован')
    )

    name = models.CharField('Название', max_length=80)
    description = models.TextField('Описание', null=True, blank=True)
    photo = models.ImageField('Фотография', null=True, blank=True, upload_to='photo_post/')
    status = models.CharField('Статус публикации', max_length=200, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    name = models.CharField('Название категории', max_length=50)
    rating = models.PositiveSmallIntegerField('Рейтинг', choices=RATING_CHOICES, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.rating}'
