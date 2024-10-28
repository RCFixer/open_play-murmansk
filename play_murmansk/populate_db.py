import os
import django

# Устанавливаем переменные окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_murmansk.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from ads.models import Ad, AdComment, AdCategory
from core.models import OnlineUser, Guest
from forum.models import ForumSection, ForumSubsection, ForumTopic, ForumMessage
from news.models import News, NewsComment
from reviews.models import Review, ReviewComment

User = get_user_model()

# Создаем пользователей
user1 = User.objects.create_user(username='user1', password='password1', email='user1@example.com')
user2 = User.objects.create_user(username='user2', password='password2', email='user2@example.com')

# Создаем объекты для модуля ads
ad1 = Ad.objects.create(
    title='Продам PS5',
    content='Продам PS5 в отличном состоянии.',
    image='ads/ps5.jpg',
    category=AdCategory.SELL,
    author=user1
)

ad2 = Ad.objects.create(
    title='Продам Xbox Series X',
    content='Продам Xbox в отличном состоянии.',
    image='ads/xbox.jpg',
    category=AdCategory.SELL,
    author=user1
)

ad3 = Ad.objects.create(
    title='Продам Xbox Series S',
    content='Продам Xbox S в отличном состоянии.',
    image='ads/xboxs.jpg',
    category=AdCategory.SELL,
    author=user1
)

AdComment.objects.create(
    ad=ad1,
    author=user2,
    content='Сколько стоит?'
)

# Создаем объекты для модуля core
OnlineUser.objects.create(user=user1)
Guest.objects.create(session_key='guest_session_1')

# Создаем объекты для модуля forum
section1 = ForumSection.objects.create(title='Раздел 1')
subsection1 = ForumSubsection.objects.create(section=section1, title='Подраздел 1')
topic1 = ForumTopic.objects.create(subsection=subsection1, title='Тема 1', author=user1)
ForumMessage.objects.create(topic=topic1, author=user2, content='Первое сообщение в теме 1')

# Создаем объекты для модуля news
news1 = News.objects.create(
    title='Новость 1',
    content='Содержание новости 1',
    image='news/news1.jpg',
    source='http://example.com',
    author=user1
)

news2 = News.objects.create(
    title='Новость 2',
    content='Содержание новости 2',
    image='news/news1.jpg',
    source='http://example.com',
    author=user1
)

news3 = News.objects.create(
    title='Новость 3',
    content='Содержание новости 3',
    image='news/news1.jpg',
    source='http://example.com',
    author=user1
)

NewsComment.objects.create(
    news=news1,
    author=user2,
    content='Комментарий к новости 1'
)

# Создаем объекты для модуля reviews
review1 = Review.objects.create(
    title='Обзор 1',
    content='Содержание обзора 1',
    image='reviews/review1.jpg',
    author=user1
)

review2 = Review.objects.create(
    title='Обзор 2',
    content='Содержание обзора 2',
    image='reviews/review1.jpg',
    author=user1
)

review3 = Review.objects.create(
    title='Обзор 3',
    content='Содержание обзора 3',
    image='reviews/review1.jpg',
    author=user1
)

ReviewComment.objects.create(
    review=review1,
    author=user2,
    content='Комментарий к обзору 1'
)

print("База данных успешно наполнена тестовыми данными.")