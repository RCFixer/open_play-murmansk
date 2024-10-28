from django.db import models
from django.conf import settings

from core.models import BaseComment

class AdCategory(models.TextChoices):
    SELL = 'sell', 'Продам'
    BUY = 'buy', 'Куплю'
    EXCHANGE = 'exchange', 'Обменяю'
    VARIOUS = 'various', 'Разное'
    SERVICES = 'services', 'Услуги'

class Ad(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='ads/')
    category = models.CharField(max_length=10, choices=AdCategory.choices)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AdComment(BaseComment):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.ad.title}"
