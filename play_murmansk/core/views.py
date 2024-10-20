from django.views.generic import TemplateView
from django.utils import timezone
from django.db.models import Count
from news.models import News, NewsComment
from ads.models import Ad
from reviews.models import Review
from forum.models import ForumTopic, ForumMessage
from .models import OnlineUser, Guest

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Online users and guests
        context['online_users'] = OnlineUser.objects.filter(last_seen__gte=timezone.now() - timezone.timedelta(minutes=5))
        context['guest_count'] = Guest.objects.filter(last_seen__gte=timezone.now() - timezone.timedelta(minutes=5)).count()

        # Top 20 forum topics by latest messages
        context['latest_forum_topics'] = ForumTopic.objects.annotate(
            latest_message=Count('messages')
        ).order_by('-latest_message')[:20]

        # Latest 20 comments from all sections
        context['latest_comments'] = (
            NewsComment.objects.all() |
            AdComment.objects.all() |
            ReviewComment.objects.all()
        ).order_by('-created_at')[:20]

        # Latest 10 ads
        context['latest_ads'] = Ad.objects.order_by('-created_at')[:10]

        # Latest 7 reviews
        context['latest_reviews'] = Review.objects.order_by('-created_at')[:7]

        return context