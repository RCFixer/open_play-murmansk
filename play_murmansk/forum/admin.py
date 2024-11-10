from django.contrib import admin
from .models import ForumSection, ForumSubsection, ForumTopic, ForumMessage

admin.site.register(ForumSection)
admin.site.register(ForumSubsection)
admin.site.register(ForumTopic)
admin.site.register(ForumMessage)
