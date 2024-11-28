from django.urls import path
from .views import (
    ForumSectionListView, ForumTopicListView, ForumTopicDetailView,
    ForumMessageUpdateView, ForumCommentDeleteView
)

urlpatterns = [
    path('', ForumSectionListView.as_view(), name='forum_section_list'),
    path('<int:subsection_id>/topic/', ForumTopicListView.as_view(), name='forum_topic_list'),
    path('all-topics/', ForumTopicListView.as_view(), name='all_topics_list'),
    path('topic/<int:pk>/', ForumTopicDetailView.as_view(), name='forum_topic_detail'),
    path('message/<int:pk>/update/', ForumMessageUpdateView.as_view(), name='forum_message_update'),
    path('message/<int:pk>/delete/', ForumCommentDeleteView.as_view(), name='forum_message_delete'),
]