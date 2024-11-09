from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Count
from .models import News
from core.views import ViewsCount, PostInfoSaturation, PostMethodCommentForm


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10  # Указываем, сколько новостей отображать на одной странице

    def get_queryset(self):
        # Аннотируем каждую новость количеством комментариев
        queryset = News.objects.annotate(
            comments_count=Count('comments')
        ).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Теперь в context['news_list'] уже будет список новостей с подсчитанным количеством комментариев
        return context

class NewsDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, News)
        context.update(post.get_context_data())

        return context

class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'content', 'image', 'source']
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'content', 'image', 'source']
    template_name = 'news/news_form.html'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = '/news/'
