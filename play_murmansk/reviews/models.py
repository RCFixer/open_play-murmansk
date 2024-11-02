from django.db import models
from django.conf import settings
from django_prose_editor.sanitized import SanitizedProseEditorField


class Review(models.Model):
    title = models.CharField(max_length=255)
    short_content = SanitizedProseEditorField(config = {"types": ["strong", "em", "sub", "sup", "link", "underline",
                                                            "strikethrough"],
                                                  "history": True,
                                                  "typographic": True,})
    content = models.TextField()
    image = models.ImageField(upload_to='reviews/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
