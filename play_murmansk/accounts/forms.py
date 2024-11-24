from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'psn_id', 'gametag_id', 'nintendo_id', 'steam_id', 'password1', 'password2']

class CustomUserUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = CustomUser
        fields = ['avatar', 'psn_id', 'gametag_id', 'nintendo_id', 'steam_id']
