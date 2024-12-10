from django.urls import path

from .views import NewsCreateView, NewsDetailView, NewsListView

urlpatterns = [
    path("", NewsListView.as_view(), name="news"),
    path("<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("create/", NewsCreateView.as_view(), name="news_create"),
]
