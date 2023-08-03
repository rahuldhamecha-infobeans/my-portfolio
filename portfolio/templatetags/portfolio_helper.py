from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='get_sub_text')
def get_sub_text(value,param=50):
    return value[:param]+'....'