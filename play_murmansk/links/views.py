from django.views.generic import ListView, DetailView
from django.db.models import Count

from .models import Link, LinkCategory
from core.views import ViewsCount, PostInfoSaturation, PostMethodCommentForm

class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'
    context_object_name = 'link_list'

    def get_queryset(self):
        queryset = Link.objects.annotate(
            comments_count=Count('comments')
        ).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_category_list'] = LinkCategory.choices
        return context

class LinkDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Link
    template_name = 'links/link_detail.html'
    context_object_name = 'link'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Link)
        context.update(post.get_context_data())

        return context