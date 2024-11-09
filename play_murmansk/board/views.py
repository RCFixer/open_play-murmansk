from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count

from .models import Ad, AdCategory
from core.views import ViewsCount, PostInfoSaturation, PostMethodCommentForm

class BoardListView(ListView):
    model = Ad
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        queryset = Ad.objects.annotate(
            comments_count=Count('comments')
        ).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_category_list'] = AdCategory.choices
        return context

class BoardDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Ad
    template_name = 'board/board_detail.html'
    context_object_name = 'board'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Ad)
        context.update(post.get_context_data())

        return context

class BoardCreateView(CreateView):
    model = Ad
    fields = ['title', 'content', 'image', 'category']
    template_name = 'board/board_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BoardUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'content', 'image', 'category']
    template_name = 'board/board_form.html'

class BoardDeleteView(DeleteView):
    model = Ad
    template_name = 'board/board_confirm_delete.html'
    success_url = '/board/'
