from django.urls import path
from .views import (
    PublicationListView, PublicationDetailView
)

urlpatterns = [
    path('', PublicationListView.as_view(), name='publ_list'),
    path('<int:pk>/', PublicationDetailView.as_view(), name='publ_detail'),
]
