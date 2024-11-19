from django.db import models
from django.conf import settings
from django_prose_editor.sanitized import SanitizedProseEditorField
from django.contrib.contenttypes.fields import GenericRelation

from core.models import CommonComment


class LinkCategory(models.TextChoices):
    ONLINE_STORES = 'Интернет-магазины'
    OFFICIALLY = 'Официально'
    GOOD_TO_KNOW = 'Полезно'

class Link(models.Model):
    title = models.CharField(max_length=255)
    content = SanitizedProseEditorField(config = {"types": ["strong", "em", "sub", "sup", "link", "underline",
                                                            "strikethrough"],
                                                  "history": True,
                                                  "typographic": True,})
    image = models.ImageField(upload_to='link/')
    category = models.CharField(max_length=128, choices=LinkCategory.choices)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    comments = GenericRelation(CommonComment)

    def __str__(self):
        return self.title
