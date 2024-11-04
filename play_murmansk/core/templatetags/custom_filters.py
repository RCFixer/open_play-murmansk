from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def strip_p_tags(value):
    return value.replace('<p>', '').replace('</p>', '')
