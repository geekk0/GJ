# Generated by Django 3.0.4 on 2020-08-08 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200727_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='media/default.png', upload_to='', verbose_name='Картинки')),
                ('photo_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
