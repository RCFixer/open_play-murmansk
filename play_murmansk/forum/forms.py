from django import forms
from .models import ForumMessage, ForumTopic

class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.topic = kwargs.pop('topic_object', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.topic = self.topic

        if commit:
            comment.save()
        return comment


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['subsection', 'title', 'description']