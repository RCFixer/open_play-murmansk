from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News, NewsComment

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

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

class NewsCommentCreateView(CreateView):
    model = NewsComment
    fields = ['content']
    template_name = 'news/news_comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.news_id = self.kwargs['pk']
        return super().form_valid(form)

class NewsCommentUpdateView(UpdateView):
    model = NewsComment
    fields = ['content']
    template_name = 'news/news_comment_form.html'

class NewsCommentDeleteView(DeleteView):
    model = NewsComment
    template_name = 'news/news_comment_confirm_delete.html'
    success_url = '/news/'
