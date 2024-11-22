from django import template

register = template.Library()

@register.filter
def strip_p_tags(value):
    # Это надо чтобы комментарии отображались без отступов сверху и снизу, так как <p> создаёт их тут
    return value.replace('<p>', '').replace('</p>', '')

@register.filter
def strip_p_tags_for_news_list(value):
    # Это надо чтобы новости отображались без отступов сверху и снизу, так как <p> создаёт их тут
    return value.replace('<p>', '').replace('</p>', '<br><br>')

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key[0])