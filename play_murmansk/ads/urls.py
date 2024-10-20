from django.urls import path
from .views import (
    AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView,
    AdCommentCreateView, AdCommentUpdateView, AdCommentDeleteView
)

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('<int:pk>/comment/create/', AdCommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/update/', AdCommentUpdateView.as_view(), name='ad_comment_update'),
    path('comment/<int:pk>/delete/', AdCommentDeleteView.as_view(), name='ad_comment_delete'),
]
