from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from core.views import PostInfoSaturation, PostMethodCommentForm, ViewsCount

from .forms import ReviewForm
from .models import Review


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "review_list"
    paginate_by = 10  # Указываем, сколько новостей отображать на одной странице

    def get_queryset(self):
        # Аннотируем каждую новость количеством комментариев
        queryset = Review.objects.annotate(comments_count=Count("comments")).order_by(
            "-id"
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReviewDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Review
    template_name = "reviews/review_detail.html"
    context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Review)
        context.update(post.get_context_data())

        return context


@method_decorator(login_required, name="dispatch")
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Перенаправление на детальную страницу созданного объявления
        return reverse("review_detail", kwargs={"pk": self.object.pk})
