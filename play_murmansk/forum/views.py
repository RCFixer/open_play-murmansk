from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import OuterRef, Subquery, Count
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
        ) # Todo переделать всё на один подзапрос!

        # Получаем все ForumSection с подсекциями и последним сообщением
        queryset = ForumSection.objects.prefetch_related(
            models.Prefetch('subsections', queryset=subsections)
        )

        return queryset

class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topic_list'
    paginate_by = 5

    def get_queryset(self):
        subsection_id = self.kwargs.get('subsection_id')

        # Фильтруем темы по subsection_id
        queryset = ForumTopic.objects.filter(subsection_id=subsection_id)

        # Добавляем количество сообщений в каждой теме
        queryset = queryset.annotate(
            message_count=Count('messages')
        )

        # Добавляем информацию о последнем сообщении в каждой теме
        last_message_subquery = ForumMessage.objects.filter(
            topic=OuterRef('pk')
        ).order_by('-created_at').values('author__username', 'created_at')[:1]

        queryset = queryset.annotate(
            last_message_author=Subquery(last_message_subquery.values('author__username')),
            last_message_time=Subquery(last_message_subquery.values('created_at'))
        ).order_by('-id')

        # Разделяем queryset на две части
        pinned_topics = queryset.filter(is_pinned=True).order_by('-id')
        unpinned_topics = queryset.filter(is_pinned=False).order_by('-id')

        # Сохраняем pinned_topics для передачи в контекст
        self.pinned_topics = pinned_topics

        return unpinned_topics

        # return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsection_id'] = self.kwargs.get('subsection_id')
        context['pinned_topics'] = self.pinned_topics
        context['current_topics'] = len(self.pinned_topics) + len(context['topic_list'])
        context['all_topics'] = len(self.pinned_topics) + len(self.object_list)
        return context

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
