from django.urls import path
from .views import (
    BoardListView, BoardDetailView, BoardCreateView
)

urlpatterns = [
    path('', BoardListView.as_view(), name='boards'),
    path('<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('create/', BoardCreateView.as_view(), name='board_create'),
]
