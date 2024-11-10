from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import OuterRef, Subquery
from django.db import models

from .models import ForumSection, ForumSubsection, ForumTopic, ForumMessage

class ForumSectionListView(ListView):
    model = ForumSection
    template_name = 'forum/section_list.html'
    context_object_name = 'section_list'

    def get_queryset(self):
        # Получаем последнее сообщение в каждой ForumSubsection
        last_message_subquery = ForumMessage.objects.filter(
            topic__subsection=OuterRef('pk')
        ).order_by('-created_at').values(
            'created_at', 'topic__title', 'author__username'
        )[:1]

        # Получаем все ForumSubsection с последним сообщением
        subsections = ForumSubsection.objects.annotate(
            last_message_created_at=Subquery(last_message_subquery.values('created_at')),
            last_message_topic_title=Subquery(last_message_subquery.values('topic__title')),
            last_message_author_username=Subquery(last_message_subquery.values('author__username')),
        )

        # Получаем все ForumSection с подсекциями и последним сообщением
        queryset = ForumSection.objects.prefetch_related(
            models.Prefetch('subsections', queryset=subsections)
        )

        return queryset

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
