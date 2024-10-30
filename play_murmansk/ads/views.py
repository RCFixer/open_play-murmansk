from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Ad, AdCategory

class AdListView(TemplateView):
    template_name = 'ads/ad_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_list'] = Ad.objects.all()
        context['ad_category_list'] = AdCategory.choices
        return context

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
