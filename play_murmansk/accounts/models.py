from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class CustomUser(AbstractUser):
    # Поле для аватара, с указанием пути к изображению по умолчанию
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg', blank=True)

    # Поля для игровых ID
    psn_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='PSN ID')
    gametag_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Game Tag ID')
    nintendo_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nintendo ID')
    steam_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Steam ID')

    def save(self, *args, **kwargs):
        # Сначала вызовем метод родителя, чтобы сохранить оригинальное изображение
        super().save(*args, **kwargs)

        # Теперь откроем сохранённое изображение и изменим его размеры
        img_path = self.avatar.path
        with Image.open(img_path) as img:
            # Укажите желаемое разрешение
            max_resolution = (200, 200)  # Ширина x Высота

            # Сжимаем изображение
            img.thumbnail(max_resolution)

            # Сохраняем изображение (перезаписываем файл)
            img.save(img_path)