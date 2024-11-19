from django.urls import path
from .views import (
    LinkListView, LinkDetailView
)

urlpatterns = [
    path('', LinkListView.as_view(), name='links'),
    path('<int:pk>/', LinkDetailView.as_view(), name='link_detail')
]
