from django.db import models
from django.conf import settings

class OnlineUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Guest(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_key

class BaseComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Comment by {self.author.username}"
