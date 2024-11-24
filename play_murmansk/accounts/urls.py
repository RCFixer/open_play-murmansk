from django.urls import path
from .views import register, profile, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
]