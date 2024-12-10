from django.utils.timezone import now, timedelta

from .models import UserActivity


def clean_old_user_activity():
    ten_minutes_ago = now() - timedelta(minutes=10)
    deleted_count, _ = UserActivity.objects.filter(
        last_activity__lt=ten_minutes_ago
    ).delete()
    return deleted_count
