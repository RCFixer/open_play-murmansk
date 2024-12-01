from django.utils.timezone import now, timedelta
from django.db.models import F, Max

from .models import UserActivity
from core.models import CommonComment, Advertisement, UpcomingGame
from forum.models import ForumTopic
from reviews.models import Review
from board.models import Board
from .forms import CustomAuthenticationForm
from .utils import clean_old_user_activity

def latest_comments(request):
    latest_comments_list = CommonComment.objects.order_by('-id')[:20]
    return {'latest_comments': latest_comments_list}

def latest_forum_topics(request):
    latest_forum_topics_list = ForumTopic.objects.order_by('-id')[:20]
    return {'latest_forum_topics': latest_forum_topics_list}

def latest_reviews(request):
    latest_reviews_list = Review.objects.order_by('-id')[:7]
    return {'latest_reviews': latest_reviews_list}

def latest_boards(request):
    latest_boards_list = Board.objects.order_by('-id')[:10]
    return {'latest_boards': latest_boards_list}

def load_ads(request):
    advertisements = Advertisement.objects.all()
    return {'advertisements': advertisements}

def upcoming_game(request):
    latest_upcoming_game = UpcomingGame.objects.last()
    return {'latest_upcoming_game': latest_upcoming_game}

def login_form_processor(request):
    """
    Контекстный процессор для добавления формы авторизации.
    """
    return {'login_form': CustomAuthenticationForm()}

def get_recent_activity(request):
    thirty_minutes_ago = now() - timedelta(minutes=10)

    # Проверка самой старой записи без cron
    # Закоментить если на хостинге будет cron
    oldest_record = UserActivity.objects.first()
    if oldest_record and oldest_record.last_activity < thirty_minutes_ago:
        # Если самая старая запись старше 10 минут, проводим очистку
        clean_old_user_activity()

    # Раскоментить когда на Postgre перейду на проде
    # activities = UserActivity.objects.filter(last_activity__gte=thirty_minutes_ago)
    #
    # active_users = activities.filter(user__isnull=False).distinct('user').count()
    # active_guests = activities.filter(user__isnull=True).distinct('session_key').count()

    # А этот ужас посвящается SQLite
    # Уникальные активные пользователи
    active_users = list(
        UserActivity.objects.filter(last_activity__gte=thirty_minutes_ago, user__isnull=False)
        .values('user', 'user__username', 'user__email')
        .annotate(last_activity=Max('last_activity'))
    )

    # Уникальные активные гости
    active_guests = (
        UserActivity.objects.filter(last_activity__gte=thirty_minutes_ago, user__isnull=True)
        .values('session_key')  # Группируем по session_key
        .annotate(last_activity=Max('last_activity'))  # Берем последнее обновление
        .count()
    )

    return {
        "active_users": active_users,
        "active_guests": active_guests,
        "total_users_count": len(active_users) + active_guests,
    }
