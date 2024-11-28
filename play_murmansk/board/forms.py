from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'content', 'image', 'category']
        labels = {
            'title': 'Заголовок объявления',
            'content': 'Текст объявления',
            'image': 'Изображение',
            'category': 'Категория',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'placeholder': 'Введите текст'}),
            'image': forms.ClearableFileInput(attrs={}),
            'category': forms.Select(attrs={}),
        }