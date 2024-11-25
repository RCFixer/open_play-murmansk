from django.urls import path
from .views import CommentDeleteView

urlpatterns = [
    # Другие маршруты
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
