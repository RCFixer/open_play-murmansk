from django.urls import path
from .views import (
    ForumSectionListView, ForumTopicListView, ForumTopicDetailView,
    ForumMessageCreateView, ForumMessageUpdateView, ForumMessageDeleteView
)

urlpatterns = [
    path('', ForumSectionListView.as_view(), name='forum_section_list'),
    path('<int:subsection_id>/topic/', ForumTopicListView.as_view(), name='forum_topic_list'),
    path('topic/<int:pk>/', ForumTopicDetailView.as_view(), name='forum_topic_detail'),
    path('topic/<int:pk>/message/create/', ForumMessageCreateView.as_view(), name='forum_message_create'),
    path('message/<int:pk>/update/', ForumMessageUpdateView.as_view(), name='forum_message_update'),
    path('message/<int:pk>/delete/', ForumMessageDeleteView.as_view(), name='forum_message_delete'),
]