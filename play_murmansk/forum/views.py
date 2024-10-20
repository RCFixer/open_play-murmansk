from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ForumSection, ForumSubsection, ForumTopic, ForumMessage

class ForumSectionListView(ListView):
    model = ForumSection
    template_name = 'forum/section_list.html'
    context_object_name = 'section_list'

class ForumSubsectionListView(ListView):
    model = ForumSubsection
    template_name = 'forum/subsection_list.html'
    context_object_name = 'subsection_list'

class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topic_list'

class ForumTopicDetailView(DetailView):
    model = ForumTopic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'

class ForumMessageCreateView(CreateView):
    model = ForumMessage
    fields = ['content']
    template_name = 'forum/message_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic_id = self.kwargs['pk']
        return super().form_valid(form)

class ForumMessageUpdateView(UpdateView):
    model = ForumMessage
    fields = ['content']
    template_name = 'forum/message_form.html'

class ForumMessageDeleteView(DeleteView):
    model = ForumMessage
    template_name = 'forum/message_confirm_delete.html'
    success_url = '/forum/'
