from django.db import models
from django.conf import settings


class Review(models.Model):
    title = models.CharField(max_length=255)
    short_content = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='reviews/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
