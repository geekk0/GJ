from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, default='Название события', verbose_name='Название')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    photo = models.ImageField(upload_to='', default='media/default.png', verbose_name='Картинки')


    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
            return self.title



# Create your models here.
