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

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )