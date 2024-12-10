from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "short_content", "content", "image"]
        labels = {
            "title": "Заголовок объявления",
            "short_content": "Краткое описание",
            "content": "Текст статьи",
            "image": "Обложка обзора",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Введите заголовок"}),
            "short_content": forms.Textarea(
                attrs={"placeholder": "Введите краткое описание"}
            ),
            "content": SummernoteWidget(),
            "image": forms.ClearableFileInput(attrs={}),
        }
