from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Publication


# Apply summernote to all TextField in model.
class PublicationAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ("content",)


admin.site.register(Publication, PublicationAdmin)
