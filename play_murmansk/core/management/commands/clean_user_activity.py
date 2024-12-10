from django.core.management.base import BaseCommand

from core.models import UserActivity
from core.utils import clean_old_user_activity


class Command(BaseCommand):
    help = "Clean old user activity records"

    def handle(self, *args, **kwargs):
        deleted_count = clean_old_user_activity()
        self.stdout.write(
            self.style.SUCCESS(f"Deleted {deleted_count} old user activity records.")
        )
