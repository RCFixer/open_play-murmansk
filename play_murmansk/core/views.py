from django.contrib.contenttypes.models import ContentType

from .models import CommonComment

def get_comments_for_object(model_object ,object_id):
    news_content_type = ContentType.objects.get_for_model(model_object)
    news_item = model_object.objects.get(id=object_id)

    comments = CommonComment.objects.filter(
        content_type=news_content_type,
        object_id=news_item.id
    )

    return comments
