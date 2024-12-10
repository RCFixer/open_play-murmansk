from django.contrib import admin

from .models import Advertisement, CommonComment, UpcomingGame

admin.site.register(CommonComment)
admin.site.register(Advertisement)
admin.site.register(UpcomingGame)
