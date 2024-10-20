from django.urls import path
from .views import (
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
    ReviewCommentCreateView, ReviewCommentUpdateView, ReviewCommentDeleteView
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('<int:pk>/comment/create/', ReviewCommentCreateView.as_view(), name='review_comment_create'),
    path('comment/<int:pk>/update/', ReviewCommentUpdateView.as_view(), name='review_comment_update'),
    path('comment/<int:pk>/delete/', ReviewCommentDeleteView.as_view(), name='review_comment_delete'),
]
