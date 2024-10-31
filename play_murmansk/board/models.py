from django.db import models
from django.conf import settings


class AdCategory(models.TextChoices):
    SELL = 'ПРОДАМ'
    BUY = 'КУПЛЮ'
    EXCHANGE = 'ОБМЕНЯЮ'
    VARIOUS = 'РАЗНОЕ'
    SERVICES = 'УСЛУГИ'

class Ad(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='board/')
    category = models.CharField(max_length=10, choices=AdCategory.choices)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
