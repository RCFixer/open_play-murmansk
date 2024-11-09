from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count

from .models import Review
from core.views import ViewsCount, PostInfoSaturation, PostMethodCommentForm

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'review_list'
    paginate_by = 10  # Указываем, сколько новостей отображать на одной странице

    def get_queryset(self):
        # Аннотируем каждую новость количеством комментариев
        queryset = Review.objects.annotate(
            comments_count=Count('comments')
        ).order_by('-id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ReviewDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Review)
        context.update(post.get_context_data())

        return context

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'content', 'image']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'content', 'image']
    template_name = 'reviews/review_form.html'

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = '/reviews/'
