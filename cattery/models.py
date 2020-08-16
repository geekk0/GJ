from django.db import models
from django.utils import timezone


class CatCard(models.Model):
    name = models.TextField(max_length=20, verbose_name='Имя')
    photo = models.ImageField(upload_to='', default='media/default.png', verbose_name='Ссылка картинки')
    color = models.TextField(max_length=30, verbose_name='Окрас')
    birthday = models.DateField(default=timezone.now, verbose_name='День рождения')
    owner = models.TextField(max_length=20, verbose_name='Хозяин')

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'Личные дела'
        verbose_name_plural = 'Личные дела'



