from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'psn_id', 'gametag_id', 'nintendo_id', 'steam_id', 'avatar')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'avatar')}),
        ('Game IDs', {'fields': ('psn_id', 'gametag_id', 'nintendo_id', 'steam_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
