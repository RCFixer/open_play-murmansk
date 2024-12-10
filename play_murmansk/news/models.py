from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django_prose_editor.sanitized import SanitizedProseEditorField

from core.models import CommonComment
from core.views import CompressImage


class News(CompressImage, models.Model):
    title = models.CharField(max_length=255)
    content = SanitizedProseEditorField(
        config={
            "types": [
                "strong",
                "em",
                "sub",
                "sup",
                "link",
                "underline",
                "strikethrough",
            ],
            "history": True,
            "typographic": True,
        }
    )
    image = models.ImageField(blank=True, null=True, upload_to="news/")
    source = models.URLField(
        blank=True,
        null=True,
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    comments = GenericRelation(CommonComment)

    def __str__(self):
        return self.title
