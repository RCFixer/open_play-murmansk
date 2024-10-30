from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'review_list'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

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
