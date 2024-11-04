from core.models import CommonComment, Advertisement, UpcomingGame
from forum.models import ForumTopic
from reviews.models import Review
from board.models import Ad

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
    latest_boards_list = Ad.objects.order_by('-id')[:10]
    return {'latest_boards': latest_boards_list}

def load_ads(request):
    advertisements = Advertisement.objects.all()
    return {'advertisements': advertisements}

def upcoming_game(request):
    latest_upcoming_game = UpcomingGame.objects.last()
    return {'latest_upcoming_game': latest_upcoming_game}