import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, default='Название события', verbose_name='Название')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    photo = models.ImageField(upload_to='', default='media/default.png', verbose_name='Картинки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
            return self.title


class Post_images(models.Model):
    photo_of = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Относится к записи')
    image = models.ImageField(upload_to='', default='media/default.png', verbose_name='Загрузить фото')

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
        return str(self.photo_of)

