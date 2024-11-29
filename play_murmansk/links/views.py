from django.views.generic import ListView, DetailView
from django.db.models import Count

from .models import Link, LinkCategory
from core.views import ViewsCount, PostInfoSaturation, PostMethodCommentForm

class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'
    context_object_name = 'link_list'
    paginate_by = 10

    def get_queryset(self):
        category_filter = self.request.GET.get('category')

        queryset = Link.objects.annotate(
            comments_count=Count('comments')
        ).order_by('-id')
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_counts = Link.objects.values('category').annotate(
            count=Count('id')
        )

        # Преобразование в словарь
        category_counts_dict = {item['category']: item['count'] for item in category_counts}

        # Добавление в контекст
        context['link_category_counts'] = category_counts_dict
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