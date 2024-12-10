from django.urls import path

from .views import (ForumCommentDeleteView, ForumSectionListView,
                    ForumTopicCreateView, ForumTopicDetailView,
                    ForumTopicListView)

urlpatterns = [
    path("", ForumSectionListView.as_view(), name="forum_section_list"),
    path(
        "<int:subsection_id>/topic/",
        ForumTopicListView.as_view(),
        name="forum_topic_list",
    ),
    path("all-topics/", ForumTopicListView.as_view(), name="all_topics_list"),
    path("topic/<int:pk>/", ForumTopicDetailView.as_view(), name="forum_topic_detail"),
    path(
        "message/<int:pk>/delete/",
        ForumCommentDeleteView.as_view(),
        name="forum_message_delete",
    ),
    path("create-topic/", ForumTopicCreateView.as_view(), name="create_topic"),
]
