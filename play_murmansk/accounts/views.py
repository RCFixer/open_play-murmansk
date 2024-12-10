from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, CustomUserUpdateForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Авторизация пользователя после регистрации
            return redirect("profile")  # Перенаправление в личный кабинет
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/registration.html", {"form": form})


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def update_profile(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, "accounts/update_profile.html", {"form": form})
