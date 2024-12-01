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

@register.filter
def translate_category(key):
    categories = {
        'SELL': 'ПРОДАМ',
        'BUY': 'КУПЛЮ',
        'EXCHANGE': 'ОБМЕНЯЮ',
        'VARIOUS': 'РАЗНОЕ',
        'SERVICES': 'УСЛУГИ',
    }
    return categories.get(key, None)

@register.filter
def get_object_detail_url(key):
    # if key == 'ad':
    #     key = 'board'
    return f'{key}_detail'