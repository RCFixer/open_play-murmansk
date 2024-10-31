from core.models import CommonComment
from forum.models import ForumTopic
from reviews.models import Review
from board.models import Ad

def latest_comments(request):
    latest_comments_list = CommonComment.objects.order_by('-id')[:10]
    return {'latest_comments': latest_comments_list}

def latest_forum_topics(request):
    latest_forum_topics_list = ForumTopic.objects.order_by('-id')[:10]
    return {'latest_forum_topics': latest_forum_topics_list}

def latest_reviews(request):
    latest_reviews_list = Review.objects.order_by('-id')[:10]
    return {'latest_reviews': latest_reviews_list}

def latest_ads(request):
    latest_ads_list = Ad.objects.order_by('-id')[:10]
    return {'latest_ads': latest_ads_list}
