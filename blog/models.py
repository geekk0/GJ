
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

    class Meta:
        verbose_name = 'Статьи блога'
        verbose_name_plural = 'Статьи блога'


class PostImages(models.Model):
    photo_of = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Относится к посту')
    image = models.ImageField(upload_to='', default='media/default.png', verbose_name='Загрузить фото')
    test_field = models.CharField(max_length=2000, default='Подпись картинки', verbose_name='Подпись картинки')

    def get_images(self):
        return self.image.all()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        full_name = str(self.photo_of)+' '+' '+self.test_field
        return str(full_name)

    class Meta:
        verbose_name = 'Картинки к постам'
        verbose_name_plural = 'Картинки к постам'

