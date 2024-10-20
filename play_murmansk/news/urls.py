from django.urls import path
from .views import (
    NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    NewsCommentCreateView, NewsCommentUpdateView, NewsCommentDeleteView
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/comment/create/', NewsCommentCreateView.as_view(), name='news_comment_create'),
    path('comment/<int:pk>/update/', NewsCommentUpdateView.as_view(), name='news_comment_update'),
    path('comment/<int:pk>/delete/', NewsCommentDeleteView.as_view(), name='news_comment_delete'),
]
