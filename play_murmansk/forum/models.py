from django.conf import settings
from django.db import models
from django_prose_editor.sanitized import SanitizedProseEditorField


class ForumSection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ForumSubsection(models.Model):
    section = models.ForeignKey(
        ForumSection, on_delete=models.CASCADE, related_name="subsections"
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    topic_count = models.PositiveIntegerField(default=0)
    message_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ForumTopic(models.Model):
    subsection = models.ForeignKey(
        ForumSubsection,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name="Подраздел",
    )
    title = models.CharField(max_length=255, verbose_name="Название темы обсуждения")
    description = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Короткое описание"
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ForumMessage(models.Model):
    topic = models.ForeignKey(
        ForumTopic, on_delete=models.CASCADE, related_name="messages"
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.author.username} on {self.topic.title}"
