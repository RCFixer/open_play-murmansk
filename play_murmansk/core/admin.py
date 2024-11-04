from django.contrib import admin
from .models import CommonComment, Advertisement, UpcomingGame

admin.site.register(CommonComment)
admin.site.register(Advertisement)
admin.site.register(UpcomingGame)
