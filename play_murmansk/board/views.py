from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Ad, AdCategory

class BoardListView(TemplateView):
    template_name = 'board/board_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_list'] = Ad.objects.all()
        context['board_category_list'] = AdCategory.choices
        return context

class BoardDetailView(DetailView):
    model = Ad
    template_name = 'board/board_detail.html'
    context_object_name = 'board'

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
