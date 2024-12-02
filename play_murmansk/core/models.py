from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django_prose_editor.sanitized import SanitizedProseEditorField
from django.utils.timezone import now
from PIL import Image

from accounts.models import CustomUser


class CompressImage:

    def save(self, *args, **kwargs):
        # Сначала вызовем метод родителя, чтобы сохранить оригинальное изображение
        super().save(*args, **kwargs)

        # Теперь откроем сохранённое изображение и изменим его размеры
        img_path = self.image.path
        with Image.open(img_path) as img:
            # Укажите желаемое разрешение
            max_resolution = (500, 500)  # Ширина x Высота

            # Сжимаем изображение
            img.thumbnail(max_resolution)

            # Сохраняем изображение (перезаписываем файл)
            img.save(img_path)


class CommonComment(models.Model):
    object_id = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = SanitizedProseEditorField(config = {"types": ["strong", "em", "sub", "sup", "link", "underline",
                                                            "strikethrough"],
                                                  "history": True,
                                                  "typographic": True,})
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comment by {self.author.username}"

class Advertisement(CompressImage, models.Model):
    image = models.ImageField(upload_to='advertisements/', verbose_name='Картинка')
    link = models.URLField(verbose_name='Ссылка')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    def __str__(self):
        return f"Advertisement #{self.id}"

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

class UpcomingGame(CompressImage, models.Model):
    image = models.ImageField(upload_to='upcoming_games/', verbose_name='Картинка')
    game_title = models.CharField(max_length=40, verbose_name='Название игры')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return f"Upcoming Game #{self.id}"

    class Meta:
        verbose_name = 'Ждем и Верим'
        verbose_name_plural = 'Ждем и Верим'

class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    last_activity = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user if self.user else 'Guest'} - {self.last_activity}"