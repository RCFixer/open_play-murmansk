from django.db import models
from django.conf import settings
from django_prose_editor.sanitized import SanitizedProseEditorField
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _

from core.models import CommonComment
from core.views import CompressImage


class BoardCategory(models.TextChoices):
    SELL = 'SELL', _('ПРОДАМ')
    BUY = 'BUY', _('КУПЛЮ')
    EXCHANGE = 'EXCHANGE', _('ОБМЕНЯЮ')
    VARIOUS = 'VARIOUS', _('РАЗНОЕ')
    SERVICES = 'SERVICES', _('УСЛУГИ')

class Board(CompressImage, models.Model):
    title = models.CharField(max_length=255)
    content = SanitizedProseEditorField(config = {"types": ["strong", "em", "sub", "sup", "link", "underline",
                                                            "strikethrough"],
                                                  "history": True,
                                                  "typographic": True,})
    image = models.ImageField(blank=True, null=True, upload_to='board/')
    category = models.CharField(max_length=10, choices=BoardCategory.choices)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    comments = GenericRelation(CommonComment)

    def __str__(self):
        return self.title
