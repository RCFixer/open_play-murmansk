from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Поле для аватара, с указанием пути к изображению по умолчанию
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg', blank=True)

    # Поля для игровых ID
    psn_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='PSN ID')
    gametag_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Game Tag ID')
    nintendo_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nintendo ID')
    steam_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Steam ID')
