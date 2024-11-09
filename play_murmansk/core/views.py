from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from .models import CommonComment
from core.forms import CommonCommentForm
from news.models import News


def get_comments_count_for_object(model_object, object_id):
    news_content_type = ContentType.objects.get_for_model(model_object)
    news_item = model_object.objects.get(id=object_id)
    comments_count = CommonComment.objects.filter(
        content_type=news_content_type,
        object_id=news_item.id
    ).count()
    return comments_count

class ViewsCount:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views += 1
        obj.save()

        return obj

class PostInfoSaturation:

    def __init__(self, post_object, post_request):
        self.object = post_object
        self.request = post_request

    def get_comment_form(self):
        news_item = self.object
        return CommonCommentForm(author=self.request.user, content_object=news_item)

    def get_comments_for_object(self, model_object, object_id):
        news_content_type = ContentType.objects.get_for_model(model_object)
        news_item = model_object.objects.get(id=object_id)
        comments = CommonComment.objects.filter(
            content_type=news_content_type,
            object_id=news_item.id
        )
        return comments

    def get_context_data(self):
        context = dict()
        context['form'] = self.get_comment_form()
        comments = self.get_comments_for_object(News, self.object.id)
        context['comments'] = comments
        context['form'] = CommonCommentForm(author=self.request.user, content_object=self.object)

        return context

class PostMethodCommentForm:

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        news_item = self.object

        form = CommonCommentForm(request.POST, author=request.user, content_object=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=news_item.id)  # Перенаправление на ту же страницу

        context = self.get_context_data(object=news_item)
        context['form'] = form
        return self.render_to_response(context)
