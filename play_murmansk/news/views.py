from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import News
from core.views import get_comments_for_object
from core.views import ViewsCount

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

class NewsDetailView(ViewsCount, DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_item = self.object

        comments = get_comments_for_object(News, news_item.id)
        context['comments'] = comments

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
