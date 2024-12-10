from django.urls import path

from .views import PublicationDetailView, PublicationListView

urlpatterns = [
    path("", PublicationListView.as_view(), name="publ_list"),
    path("<int:pk>/", PublicationDetailView.as_view(), name="publication_detail"),
]
