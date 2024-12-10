from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile, register, update_profile

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("profile/update/", update_profile, name="update_profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
]
