from django.contrib import admin

from .models import ForumMessage, ForumSection, ForumSubsection, ForumTopic

admin.site.register(ForumSection)
admin.site.register(ForumSubsection)
admin.site.register(ForumTopic)
admin.site.register(ForumMessage)
