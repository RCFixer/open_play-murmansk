from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, AdComment

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ad_list'

class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'

class AdCreateView(CreateView):
    model = Ad
    fields = ['title', 'content', 'image', 'category']
    template_name = 'ads/ad_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'content', 'image', 'category']
    template_name = 'ads/ad_form.html'

class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
    success_url = '/ads/'

class AdCommentCreateView(CreateView):
    model = AdComment
    fields = ['content']
    template_name = 'ads/ad_comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ad_id = self.kwargs['pk']
        return super().form_valid(form)

class AdCommentUpdateView(UpdateView):
    model = AdComment
    fields = ['content']
    template_name = 'ads/ad_comment_form.html'

class AdCommentDeleteView(DeleteView):
    model = AdComment
    template_name = 'ads/ad_comment_confirm_delete.html'
    success_url = '/ads/'
