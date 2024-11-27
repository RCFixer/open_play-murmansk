import datetime
from django.utils.timezone import now
from .models import UserActivity

class ActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.user.is_authenticated:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

            UserActivity.objects.update_or_create(
                session_key=session_key,
                defaults={"last_activity": now()},
            )
        else:
            UserActivity.objects.update_or_create(
                user=request.user,
                defaults={"last_activity": now()},
            )

        return response