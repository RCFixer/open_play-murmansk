from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from .models import CommonComment
from core.forms import CommonCommentForm


def get_comments_count_for_object(model_object, object_id):
    object_content_type = ContentType.objects.get_for_model(model_object)
    object_item = model_object.objects.get(id=object_id)
    comments_count = CommonComment.objects.filter(
        content_type=object_content_type,
        object_id=object_item.id
    ).count()
    return comments_count

class ViewsCount:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views += 1
        obj.save()

        return obj

class PostInfoSaturation:

    def __init__(self, post_object, post_request, post_model):
        self.object = post_object
        self.request = post_request
        self.model = post_model

    def get_comments_for_object(self, model_object, object_id):
        post_content_type = ContentType.objects.get_for_model(model_object)
        post_item = model_object.objects.get(id=object_id)
        comments = CommonComment.objects.filter(
            content_type=post_content_type,
            object_id=post_item.id
        )
        return comments

    def get_context_data(self):
        context = dict()
        comments = self.get_comments_for_object(self.model, self.object.id)
        context['comments'] = comments
        context['form'] = CommonCommentForm(author=self.request.user, content_object=self.object)

        return context

class PostMethodCommentForm:

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        object_item = self.object

        form = CommonCommentForm(request.POST, author=request.user, content_object=object_item)
        if form.is_valid():
            form.save()
            # TODO исправить костыль с редиректом!
            return redirect(f'{self.context_object_name}_detail', pk=object_item.id)  # Перенаправление на ту же страницу

        context = self.get_context_data(object=object_item)
        context['form'] = form
        return self.render_to_response(context)


class CommentDeleteView(UserPassesTestMixin, View):
    def test_func(self):
        """
        Проверяет, является ли пользователь staff.
        """
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        """
        Удаляет комментарий и возвращает JSON-ответ.
        """
        if not self.test_func():
            return JsonResponse({'error': 'Permission denied'}, status=403)

        comment_id = self.kwargs.get('pk')
        comment = get_object_or_404(CommonComment, pk=comment_id)
        comment.delete()
        return JsonResponse({'message': 'Комментарий удалён'})