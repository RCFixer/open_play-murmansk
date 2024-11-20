from django.db import models
from django.conf import settings
from django_prose_editor.sanitized import SanitizedProseEditorField
from django.contrib.contenttypes.fields import GenericRelation
from core.models import CommonComment


class Publication(models.Model):
    title = models.CharField(max_length=255)
    short_content = SanitizedProseEditorField(config = {"types": ["strong", "em", "sub", "sup", "link", "underline",
                                                            "strikethrough"],
                                                  "history": True,
                                                  "typographic": True,})
    content = models.TextField()
    image = models.ImageField(upload_to='publ/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    comments = GenericRelation(CommonComment)

    def __str__(self):
        return self.title
