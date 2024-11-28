from django.urls import path
from .views import (
    ReviewListView, ReviewDetailView, ReviewCreateView
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
]
