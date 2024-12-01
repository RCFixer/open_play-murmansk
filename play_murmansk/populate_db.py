import os
import django

# Устанавливаем переменные окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_murmansk.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from board.models import Board, BoardCategory
from forum.models import ForumSection, ForumSubsection, ForumTopic, ForumMessage
from news.models import News
from reviews.models import Review
from core.models import CommonComment

User = get_user_model()

# Создаем пользователей
user1 = User.objects.create_user(username='user1', password='password1', email='user1@example.com')
user2 = User.objects.create_user(username='user2', password='password2', email='user2@example.com')

# Создаем объекты для модуля board
ad1 = Ad.objects.create(
    title='Продам PS5',
    content='Продам PS5 в отличном состоянии.',
    image='board/ps5.jpg',
    category=BoardCategory.SELL,
    author=user1
)

ad2 = Ad.objects.create(
    title='Продам Xbox Series X',
    content='Продам Xbox в отличном состоянии.',
    image='board/xbox.jpg',
    category=BoardCategory.SELL,
    author=user1
)

ad3 = Ad.objects.create(
    title='Продам Xbox Series S',
    content='Продам Xbox S в отличном состоянии.',
    image='board/xboxs.jpg',
    category=BoardCategory.SELL,
    author=user1
)


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

# Создаем объекты для модуля reviews
review1 = Review.objects.create(
    title='Обзор 1',
    short_content='Содержание обзора 1',
    content='Большое содержание обзора 1',
    image='reviews/review1.jpg',
    author=user1
)

review2 = Review.objects.create(
    title='Обзор 2',
    short_content='Содержание обзора 2',
    content='Большое содержание обзора 2',
    image='reviews/review1.jpg',
    author=user1
)

review3 = Review.objects.create(
    title='Обзор 3',
    short_content='Содержание обзора 3',
    content='Большое содержание обзора 3',
    image='reviews/review1.jpg',
    author=user1
)


comment_ads_1 = CommonComment.objects.create(content_object=ad1, author=user2, content="Сколько стоит плойка?")
comment_ads_2 = CommonComment.objects.create(content_object=ad2, author=user2, content="Сколько стоит бокс?")
comment_ads_3 = CommonComment.objects.create(content_object=ad3, author=user2, content="Азаза, кому нужен этот обрубок?")
comment_news_1 = CommonComment.objects.create(content_object=news1, author=user2, content="Вот это новости!")
comment_news_2 = CommonComment.objects.create(content_object=news2, author=user2, content="Сони уже не те!")
comment_news_3 = CommonComment.objects.create(content_object=news3, author=user2, content="Майкрософт уже не те!")
comment_review_1 = CommonComment.objects.create(content_object=review1, author=user2, content='Классный обзор!')
comment_review_2 = CommonComment.objects.create(content_object=review2, author=user2, content='Не согласен, игра крутая!')
comment_review_3 = CommonComment.objects.create(content_object=review3, author=user2, content='Супер, прочёл на одном дыхании!')

print("База данных успешно наполнена тестовыми данными.")