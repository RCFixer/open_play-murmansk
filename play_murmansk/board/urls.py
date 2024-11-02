from django.urls import path
from .views import (
    BoardListView, BoardDetailView, BoardCreateView, BoardUpdateView, BoardDeleteView,
)

urlpatterns = [
    path('', BoardListView.as_view(), name='boards'),
    path('<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('create/', BoardCreateView.as_view(), name='board_create'),
    path('<int:pk>/update/', BoardUpdateView.as_view(), name='board_update'),
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='board_delete'),
]
