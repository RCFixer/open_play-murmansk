from django.db.models import Count
from django.views.generic import DetailView, ListView

from core.views import PostInfoSaturation, PostMethodCommentForm, ViewsCount

from .models import Publication


class PublicationListView(ListView):
    model = Publication
    template_name = "publ/publ_list.html"
    context_object_name = "publ_list"
    paginate_by = 10  # Указываем, сколько новостей отображать на одной странице

    def get_queryset(self):
        # Аннотируем каждую новость количеством комментариев
        queryset = Publication.objects.annotate(
            comments_count=Count("comments")
        ).order_by("-id")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublicationDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Publication
    template_name = "publ/publ_detail.html"
    context_object_name = "publ"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Publication)
        context.update(post.get_context_data())

        return context
