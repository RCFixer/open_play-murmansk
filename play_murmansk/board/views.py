from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from core.views import PostInfoSaturation, PostMethodCommentForm, ViewsCount

from .forms import BoardForm
from .models import Board, BoardCategory


class BoardListView(ListView):
    model = Board
    template_name = "board/board_list.html"
    context_object_name = "board_list"
    paginate_by = 10

    def get_queryset(self):
        # Получение категории из запроса
        category_filter = self.request.GET.get("category")
        queryset = Board.objects.annotate(comments_count=Count("comments"))

        # Фильтрация по категории, если указана
        if category_filter:
            queryset = queryset.filter(category=category_filter)

        return queryset.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Список категорий с подсчётом записей в каждой категории
        category_counts = Board.objects.values("category").annotate(count=Count("id"))

        # Преобразование в словарь
        category_counts_dict = {
            item["category"]: item["count"] for item in category_counts
        }

        # Добавление в контекст
        context["board_category_counts"] = category_counts_dict
        # Список всех категорий
        context["board_category_list"] = BoardCategory.choices
        # Текущая категория для отображения
        return context


class BoardDetailView(ViewsCount, DetailView, PostMethodCommentForm):
    model = Board
    template_name = "board/board_detail.html"
    context_object_name = "board"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = PostInfoSaturation(self.object, self.request, Board)
        context.update(post.get_context_data())

        return context


@method_decorator(login_required, name="dispatch")
class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm
    template_name = "board/board_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Перенаправление на детальную страницу созданного объявления
        return reverse("board_detail", kwargs={"pk": self.object.pk})
