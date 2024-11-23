from django import forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import AuthenticationForm

from .models import CommonComment

class CommonCommentForm(forms.ModelForm):
    class Meta:
        model = CommonComment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.content_object = kwargs.pop('content_object', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.content_object = self.content_object
        comment.content_type = ContentType.objects.get_for_model(self.content_object)
        comment.object_id = self.content_object.id

        if commit:
            comment.save()
        return comment


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "loginField",
                                                             'type': "text",
                                                             'name': "user",
                                                             'value': "",
                                                             'size': "20",
                                                             'style': "width:100%;",
                                                             'maxlength': "50"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "loginField",
                                                             'type': "password",
                                                             'name': "password",
                                                             'size': "20",
                                                             'style': "width:100%;",
                                                             'maxlength': "15"}))
